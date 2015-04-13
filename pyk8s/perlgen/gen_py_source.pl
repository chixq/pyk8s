use warnings;
use strict;

sub json_to_py
{
    my @jsons=<*.json>;
    foreach my $json (@jsons)
    {
        my $elem=$json;
        $elem =~ s/\.json//g;
    }
}

my $file = $ARGV[0].".json";
my %struct_items=();
my @struct_strack=();
my $targetfile= $ARGV[0].".py";

get_top_item();
#log_info();
gen_py_source();

sub get_top_item
{
    open SRC,$file or die "open $file fail\n";
    push(@struct_strack,$ARGV[0]);
    $struct_items{$ARGV[0]}="";
    while(<SRC>)
    {
        chomp();
        if(/^\s*\"(\w+)\":\s*\{}/){
            my $top_struct=$1."-S";
            $top_struct=$1."-S";
            if(exists $struct_items{$struct_strack[-1]}){
                $struct_items{$struct_strack[-1]}=$struct_items{$struct_strack[-1]}." $top_struct";
            }
            else{
                $struct_items{$struct_strack[-1]} = $top_struct;
            }
        }
        elsif(/^\s*\"(\w+)\":\s*\{/){
            my $top_struct=$1;
            if(exists $struct_items{$struct_strack[-1]}){
                $struct_items{$struct_strack[-1]}=$struct_items{$struct_strack[-1]}." $top_struct-S";
            }
            else{
                $struct_items{$struct_strack[-1]} = $top_struct."-S";
            }
            push(@struct_strack,$top_struct)
        }
        elsif(/^\s*\"items\":\s*\[/){
            my $top_struct="items";
            if(exists $struct_items{$struct_strack[-1]}){
                $struct_items{$struct_strack[-1]}=$struct_items{$struct_strack[-1]}." $top_struct-A";
            }
            else{
                $struct_items{$struct_strack[-1]} = $top_struct."-A";
            }
            my $stacknu = 1;
            while(<SRC>)
            {
                chomp();
                if(/\[/){
                    $stacknu = $stacknu+1;
                }
                elsif(/\]/){
                    $stacknu = $stacknu-1;
                    if($stacknu==0)
                    {
                        last;
                    }
                }
            }
        }
        elsif(/^\s*\"(\w+)\":\s*\[/){
            my $top_struct=$1;
            if(exists $struct_items{$struct_strack[-1]}){
                $struct_items{$struct_strack[-1]}=$struct_items{$struct_strack[-1]}." $top_struct-A";
            }
            else{
                $struct_items{$struct_strack[-1]} = $top_struct."-A";
            }
            $top_struct =~ s/s$//g;
            push(@struct_strack,$top_struct);
            while(<SRC>)
            {
                chomp();
                if(/^\s*\{/){
                    last;
                }
            }
        }
        elsif(/^\s+\{/){
            my $stacknu = 1;
            while(<SRC>)
            {
                chomp();
                if(/\{/){
                    $stacknu = $stacknu+1;
                }
                elsif(/\}/){
                    $stacknu = $stacknu-1;
                    if($stacknu==0)
                    {
                        last;
                    }
                }
            }
        }
        elsif(/\}/){
            pop(@struct_strack)
        }
        elsif(/^\s*\"(\w+)\":/){
            my $top_struct=$1."-C";
            if(exists $struct_items{$struct_strack[-1]}){
                $struct_items{$struct_strack[-1]}=$struct_items{$struct_strack[-1]}." $top_struct";
            }
            else{
                $struct_items{$struct_strack[-1]} = $top_struct;
            }
        }
    }
}

sub log_info
{
    while(my($k,$v)=each %struct_items){
        print "$k=>$v\n";
    }
}

sub gen_py_source
{
    open TAR,">$targetfile" or die "open $targetfile fail\n";
    print TAR "#!/usr/bin/env python\n";
    print TAR "# -*- coding: utf-8 -*-\n";

    print TAR "try:\n";
    print TAR "    import simplejson as json\n";
    print TAR "except ImportError:\n";
    print TAR "    import json\n";
    print TAR "import copy\n";

    print TAR "from pyk8s.exceptions import PyK8SError\n";
    while(my($k,$v)=each %struct_items){
        print "$k=>$v\n";
        print TAR "\n";
        my @items = split(" ",$v);
        my %items_map=();
        foreach my $item (@items){
            my($itemname,$type)=split(/-/,$item);
            if(exists $items_map{$itemname})
            {
                if($type eq "C")
                {
                    next;
                }
                $items_map{$itemname}=$type;
 
            }
            else
            {
                $items_map{$itemname}=$type;
            }  
        }
        if($ARGV[0] =~ /s$/){
            my $i = $ARGV[0];
            $i =~ s/s$//g;
            print TAR "from pyk8s.$i import ".ucfirst($i)."\n";
        } 
        print TAR "class ".ucfirst($k)."(object):\n";
        print TAR "    def __init__(self,**kwargs):\n";
        print TAR "        params = {\n";
        while(my($item,$type)=each %items_map){
            print TAR "            \'$item\':None,\n";
        }
        print TAR "         }\n";
        print TAR "\n";
        print TAR "        for (attribute, default_value) in params.iteritems():\n";
        print TAR "            setattr(self, attribute, kwargs.get(attribute, default_value))\n";
        print TAR "\n";
        
        print TAR "    def toDict(self):\n";
        print TAR "        params =copy.deepcopy(self.__dict__)\n";
        while(my($item,$type)=each %items_map){
            if($type eq 'A')
            {
                my $acture_item= $item;
                if($item eq "items"){
                   $acture_item = $k;
                   $acture_item =~ s/s$//g;
                }
                else
                {
                    $acture_item =~ s/s$//g;
                    if(! exists $struct_items{$acture_item})
                    {
                        next;
                    }
                }

                my $single_item = $item;
                $single_item =~ s/s$//g;
                print TAR "        i=0\n";
                print TAR "        for $single_item in self.$item:\n";
                print TAR "            params['".$item."'][i]=".$single_item.".toDict();\n";
                print TAR "            i=i+1;\n"
            }
            elsif($type eq 'S')
            {
                if(exists $struct_items{$item}){
                    print TAR "        params['$item']=self.$item.toDict();\n";
                }
            }
        }
        print TAR "        \n";
        print TAR "        return params\n";
        print TAR "\n";
        print TAR "    def toJson(self):\n";
        print TAR "        return json.dumps(self.toDict(), sort_keys=True)\n";
        print TAR "\n";
        print TAR "    \@staticmethod\n";
        print TAR "    def newFromDict(data):\n";
        print TAR "        if data is None:\n";
        print TAR "            data = {}\n";
        print TAR "\n";
        print TAR "        if not isinstance(data, dict):\n";
        print TAR "            raise PyK8SError('Type dict required')\n";
        print TAR "        else:\n";
        print TAR "            return ".ucfirst($k)."(\n";
        while(my($item,$type)=each %items_map){
            if($type eq "S")
            {
                if(! exists $struct_items{$item})
                {
                    print TAR "#";
                } 
                print TAR "                $item=".ucfirst($item).".newFromDict(data.get(\'$item\', {})),\n";
            }
            elsif($type eq "C")
            {
                print TAR "                $item=data.get('$item', None),\n";
            }
            elsif($type eq "A")
            {
                my $single_item = $item;
                if($item eq "items"){
                   $single_item = $k;
                   $single_item =~ s/s$//g;
                }
                else{
                    $single_item =~ s/s$//g;
                    if(! exists $struct_items{$single_item})
                    {
                        print TAR "#";
                    }
                }
                print TAR "                ".$item." = [".ucfirst($single_item).".newFromDict($single_item) for $single_item in (data.get('$item',{}) if (data.get('$item',{}) is not None) else {})],\n";
            }
        }
        print TAR "            )\n";
        print TAR "\n";

        print TAR "    \@staticmethod\n";
        print TAR "    def newFromJson(jsonStr):\n";
        print TAR "        try:\n";
        print TAR "            data=json.loads(jsonStr)\n";
        print TAR "        except ValueError as ex:\n";
        print TAR "            raise PyK8SError('Input json is not valid, ' + str(ex))\n";
        print TAR "        return ".ucfirst($k)."(\n";
        while(my($item,$type)=each %items_map){
            if($type eq "S")
            {
                if(! exists $struct_items{$item})
                {
                    print TAR "#";
                }
                print TAR "                $item=".ucfirst($item).".newFromDict(data.get(\'$item\', {})),\n"; 
            }
            elsif($type eq "C")
            {
                print TAR "                $item=data.get('$item', None),\n";
            }
            elsif($type eq "A")
            {
                my $single_item = $item;
                if($item eq "items"){
                   $single_item = $k;
                }
                else{
                    $single_item =~ s/s$//g;
                    if(! exists $struct_items{$single_item})
                    {
                        print TAR "#";
                    }
                }
                print TAR "                ".$item." = [".ucfirst($single_item).".newFromDict($single_item) for $single_item in (data.get('$item',{}) if (data.get('$item',{}) is not None) else {})],\n";
            }
        }
        print TAR "            )\n";
        print TAR "\n";

        print TAR "    \@staticmethod\n";
        print TAR "    def newFromJsonFile(jsonfile):\n";
        print TAR "        with open(jsonfile) as json_file:\n";
        print TAR "            json_data = json.load(json_file)\n";
        print TAR "        return ".ucfirst($k).".newFromDict(json_data)"

    }
}
