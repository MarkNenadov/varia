/* AllMyDays - Live and then die, a simulation. Implemented with a Swing
 * 	       user interface (the results are printed inside JScrollPane)
 *
 * AUTHOR
 *
 * Mark J. Nenadov (2011)
 * * Essex, Ontario
 * * Email: <marknenadov@gmail.com> 
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
 * */

package allofmydays;

import java.util.Random;
import javax.swing.*;

public class AllOfMyDays 
{
	static String[] waysToDie={"badger bite", "infected toe", "hamster attack"};
	static int ui_size_x = 500;
	static int ui_size_y = 300
	
	public static void main(String[] args) {

		int max_age = 110;
		String gui_text = "";
		
		number_my_days(max_age);
		
		JFrame frame = new JFrame("All Of My Days");
		
		for (int age=0; age < max_age; age++) {
			gui_text += live_a_year(age) + "\n";
		}
		
		gui_text += "You are now dead. You died of " + autopsy_result() + ". It happens to the best of us.";
		
		JTextArea ta = new JTextArea(gui_text); 
		frame.add(new JScrollPane(ta));
		
		frame.setSize(ui_size_x,ui_size_y);
		frame.setVisible(true);
	}

	public static String live_a_year(int age)
	{
		return "You are now " + age + " years old";
	}
	
	public static int number_my_days(int max_years)
	{
		Random randomGenerator = new Random();
		return randomGenerator.nextInt(max_years);
	}
	
	public static String autopsy_result()
	{
		Random randomGenerator = new Random();
		return waysToDie[randomGenerator.nextInt(waysToDie.length)];	
	}
}

