#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <regex.h>

char *gadaffi_pattern = "\\b[KGQ]h?add?h?af?fi\\b";
char *name_str = "Khaddafi";

int is_gadaffi_variant(char* n)
{
	int retval;
	regex_t preg;
	regcomp(&preg, gadaffi_pattern, REG_EXTENDED|REG_NOSUB);

	if (regexec(&preg, n, 0, NULL, 0) == 0) {
		retval = 1;
	}
	else {
		retval = 0;
	}
	
	regfree(&preg);

	return retval;
}	

int main()
{
	if (is_gadaffi_variant(name_str)) {
		printf("%s is a valid variant of Gadaffi\n", name_str);
	}
	else{
		printf("%s is not a valid variant of Gadaffi\n", name_str);
	}
}
