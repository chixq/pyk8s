
my $file = "endpoints.py";

open EPT,">>$file" or die "open $file fail";

print EPT "    #-------$ARGV[0]-----\n";
if($ARGV[0] =~ /s$/){
    print EPT "    def get".ucfirst($ARGV[0])."(self):\n";
    print EPT "        response = self.get('$ARGV[0]')\n";
    print EPT "        return ".ucfirst($ARGV[0]).".newFromDict(response)\n";
    print EPT "\n";
    print EPT "    def post".ucfirst($ARGV[0])."(self,params):\n";
    print EPT "        if not isinstance(params,dict):\n";
    print EPT "            raise PyK8SError('Type dict required')\n";
    print EPT "        return self.post('$ARGV[0]',params)\n";
    print EPT "\n";
    print EPT "    def add".ucfirst($ARGV[0])."(self,ob):\n";
    print EPT "        if not isinstance(ob,".ucfirst($ARGV[0])."):\n";
    print EPT "            raise PyK8SError('Type ".ucfirst($ARGV[0])." required')\n";
    print EPT "        return self.post".ucfirst($ARGV[0])."(ob.toDict())\n";
    print EPT "\n";
}
else
{
    print EPT "    def get".ucfirst($ARGV[0])."(self,name):\n";
    print EPT "        response = self.get('$ARGV[0]s/'+name)\n";
    print EPT "        return ".ucfirst($ARGV[0]).".newFromDict(response)\n";
    print EPT "\n";
    print EPT "    def post".ucfirst($ARGV[0])."(self,name,params):\n";
    print EPT "        if not isinstance(params,dict):\n";
    print EPT "            raise PyK8SError('Type dict required')\n";
    print EPT "        return self.post('$ARGV[0]s/'+name,params)\n";
    print EPT "\n";
    print EPT "    def add".ucfirst($ARGV[0])."(self,name,ob):\n";
    print EPT "        if not isinstance(ob,".ucfirst($ARGV[0])."):\n";
    print EPT "            raise PyK8SError('Type ".ucfirst($ARGV[0])." required')\n";
    print EPT "        return self.post".ucfirst($ARGV[0])."(name,ob.toDict())\n";
    print EPT "\n";
}
