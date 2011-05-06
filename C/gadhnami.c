#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <regex.h>

/* Gadhnami - Determines whether a particular name is
 * a variation of the Libyan leader Gadaffi's name.
 * 
 * A special thanks goes out to Czechnology who posted the
 * regular expression utilized here to Stack Overflow in 
 * the interesting "Regular expression to search for 
 * Gadaffi" post.
 *
 * AUTHOR
 *
 * Mark J. Nenadov (2011)
 * Essex, Ontario
 * Email: <marknenadov@gmail.com>
 *
 * LICENSING
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version
 *
 * This program is distributed in the hope that it will be useful
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>. 
 *
 */


char *gadaffi_pattern = "\\b[KGQ]h?add?h?af?fi\\b";
char *name_str = "Khaddafi";

int main()
{
   regex_t preg;
   regcomp(&preg, gadaffi_pattern, REG_EXTENDED|REG_NOSUB);
   if (regexec(&preg, name_str, 0, NULL, 0) == 0) {
	   printf("%s is a valid variant of Gadaffi\n", name_str);
   }
   else {
	   printf("%s is not a valid variant of Gadaffi\n", name_str);
   }
   regfree(&preg);

   return 0;
}
