
my $file = "endpoints.py"

open EPT,">>$file" or die "open $file fail";

print EPT "    #-------$ARGV[0]-----\n";
print EPT "    def get".ucfirst($ARGV[0])."(self):\n";
print EPT "        response = self.get('$ARGV[0]')\n";
print EPT ""
