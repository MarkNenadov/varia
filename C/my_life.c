#include <stdio.h>
#include <stdlib.h>

/* Live and then die, a simulation demonstrating rand() and srand()
 
AUTHOR

Mark J. Nenadov (2011)
Essex, Ontario
Email: <marknenadov@gmail.com> 

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

char * causes_of_death [4] = {"weasel attack", "puma kiss", "gerbil bite", "rotten artichokes"};

int number_my_days(int max_years) 
{
	srand(time(NULL));

	return rand() % max_years;
}

int live_a_year(int age)
{
	printf("Happy Birthday! You are now %d\n\n", age);
	age += 1;

	return age;
}

int face_death(int age, int max_age) {
	srand(time(NULL));
	
	int random_idx = rand() % 4;
	if (age == max_age) {
		printf("You are now dead from %s. It happens to the best of us\n", causes_of_death[random_idx]);
		return 1;
	}

	return 0;
}

int main() 
{
	int age = 0;
	int dead = 0;

	int max_age = number_my_days(110);


	printf("It's My Life! How long will I live?\n");
	while (!dead) {
		age = live_a_year(age);
		dead = face_death(age, max_age);
	}

	return 1;
}



