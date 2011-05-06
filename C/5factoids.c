#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/utsname.h>

/* Five Factoids - demonstrating simple Linux system lookups in C

AUTHOR

Mark J. Nenadov (2011)
* Essex, Ontario
* Email: <marknenadov@gmail.com> 

LICENSING

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version

This program is distributed in the hope that it will be useful
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>. 

*/

int main()
{
        int pid = getpid();
        int parent_pid = getppid();

        uid_t uid = geteuid();
        gid_t gid = getegid();

        struct utsname u;
        uname(&u);

        printf("Factoid #1: This process has an id of %d\n", pid);
        printf("Factoid #2: This process has a parent with an id of %d\n", parent_pid);

        int ret_val = system("echo");

        printf("Factoid #3: We just ran 'echo' through a system call, and the return value was: %d\n", 
	       ret_val);
        printf("Factoid #4: Your user id is %d and your group id is %d\n", (int) uid, (int) gid);
        printf("Factoid #5: The system you are using is %s release %s (version %s) on an %s\n", u.sysname,
               u.release, u.version, u.machine);

        return 0;
}

