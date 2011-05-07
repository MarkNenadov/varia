package gadhnami;

import java.io.*;
import java.util.*;
import java.util.regex.*;
import freemarker.template.*;

/* GadhnamiFreemarker
 * 
 *  (This is an alternate example of Gadhnami, which is 
 *   throwaway code to determine whether a particular name 
 *   is a varation of the Libyan leader Gadaffi's name. It
 *   demonstrates the usage of the Freemarker template
 *   engine.
 *   
 *   To get this to work, you will need to:
 *   
 *   1. put the freemarker jar file somewhere in your class 
 *      path.
 *      
 *   2. Move gadhnami.ftl into whatever path is defined 
 *      in tpl_name (or change it to suite your preference)
 *   
 * A special thanks goes out to Czechnology who posted the
 * regular expression utilized here to Stack Overflow in 
 * the interesting "Regular expression to search for 
 * Gadaffi" post.
 * 
 * - Mark J. Nenadov, 2011
 */

public class Gadhnami {
	static String working_name = "Gadaffi";
	static String gadaffi_regex = "\\b[KGQ]h?add?h?af?fi\\b";
	static String tpl_folder_name = "c:/tpl/";
	static String tpl_name = "gadhnami.ftl";
	
	static Configuration cfg;
	static Template tpl;
	static File tpl_folder;
	
	
	public static boolean isThisNameGadaffi(String name)
	{
		Pattern p = Pattern.compile(gadaffi_regex);
		Matcher m = p.matcher(name);
		
		return m.find();
	}
	
	public static Map build_hash_map(String name, boolean is_gadaffi)
	{
		Map root = new HashMap();
		root.put("name", name);
		root.put("is_gadaffi", new Boolean(is_gadaffi).toString());
		
	}
	
	public static void main(String[] args) 
	{
		tpl_folder = new File(tpl_folder_name);
		cfg = new Configuration();
		try {
			cfg.setDirectoryForTemplateLoading(tpl_folder);
		}
		catch (IOException e) {
			System.out.println("Can't open Template folder");
		}
		
		cfg.setObjectWrapper(new DefaultObjectWrapper());
		
		try {
			tpl = cfg.getTemplate(tpl_name);
		}
		catch (IOException e) {
			System.out.println("Can't open gadhnami template");
		}
		
		Writer out = new OutputStreamWriter(System.out);
		try {
			tpl.process(build_hash_map(working_name, isThisNameGadaffi(working_name)), out);
		}
		catch (TemplateException e) {
			System.out.println("tpl.process failed TemplateException");
		}
		catch (IOException e) {
			System.out.println("tpl.process failed IOException");
		}
		
		try {
			out.flush();
		}
		catch (IOException e) {
			System.out.println("out.flush failed with IOException");
		}
		
		
	}
}
