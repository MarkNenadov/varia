"""
CreatePDF - A old, scrappy wrapper for PDFlib PDF generation

(quite frankly, I don't use PDFlib anymore, I think reportlab is far
 better if you are you using Python)

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


"""

class CreatePDF:

	PDF = PDF_new()
	
	var_LineWidth = .1
	var_max_x = 0
	var_max_y = 0

	def __init__(self, filename):

		if PDF_open_file(self.PDF, filename) == -1:
			print "Couldn't open PDF file!"
			exit(2)

	def set_info(self, author, creator, title):
		
		PDF = self.PDF
		PDF_set_info(PDF, "Author", author)
		PDF_set_info(PDF, "Creator", creator)
		PDF_set_info(PDF, "Title", title)

	def set_linewidth(self, width):

		PDF_setlinewidth(self.PDF, width)
		self.var_LineWidth = width

	def init_page(self, x, y):
		self.var_max_x = x
		self.var_max_y = y
		PDF_begin_page(self.PDF, x, y)

	## -- make_text -> for text that is only 1 line -- ##

	def make_text(self, font, x, y, text, fontsize):
		PDF = self.PDF
		findfont = PDF_findfont(PDF, font, "host", 0)
		PDF_setfont(PDF, findfont, fontsize)
		PDF_set_text_pos(PDF, x, y)
		PDF_show(PDF, text)
	
	## -- make_long_text -> for text that is longer than 1 line -- ##
	
	def make_long_text(self, font, x, y, text, fontsize):
		PDF = self.PDF
		findfont = PDF_findfont(PDF, font, "host", 0)
		PDF_setfont(PDF, findfont, fontsize)
		PDF_set_text_pos(PDF, x, y)
		textlines = string.split(text,"\n")
		first = "true"
	
		for line in textlines:
			if not first == "true":
				PDF_continue_text(PDF, line)	
			else:
				PDF_show(PDF, line)			
				first = "false"
		
	def make_image(self, type, path, x, y, scale):
		PDF = self.PDF
		image = PDF_open_image_file(PDF, type, path, "", 0)
		if image == -1:
			print "Couldn't open the image file"
			exit(3)
		width = PDF_get_value(PDF, "imagewidth", image)
		height = PDF_get_value(PDF, "imageheight", image)
		PDF_place_image(PDF, image, x, y, scale)
		PDF_close_image(PDF, image)

	def make_arc(self, x_center, y_center, r, start_degree, end_degree):
		PDF_arc(self.PDF, x_center, y_center, r, start_degree, end_degree)
		PDF_closepath_fill_stroke(self.PDF)
        
	def make_line(self, from_x, from_y, to_x, to_y):
		PDF = self.PDF
		PDF_moveto(PDF, from_x, from_y)
		PDF_lineto(PDF, to_x, to_y)
		PDF_closepath_fill_stroke(PDF)
        
	def make_circle(self, x, y, r):
		PDF = self.PDF
		PDF_circle(PDF, x, y, r)
		PDF_closepath_fill_stroke(PDF)        
		
	def make_rectangle(self, top_right_x, top_right_y,
					         top_left_x, top_left_y,
					         bottom_right_x, bottom_right_y,
					         bottom_left_x, bottom_left_y):
					         
		PDF = self.PDF

		PDF_moveto(PDF, top_left_x, top_left_y)
		PDF_lineto(PDF, top_right_x, top_right_y)
		PDF_moveto(PDF, top_right_x, top_right_y)
		PDF_lineto(PDF, bottom_right_x, bottom_right_y)
		PDF_moveto(PDF, bottom_right_x, bottom_right_y)
		PDF_lineto(PDF, bottom_left_x, bottom_left_y)
		PDF_moveto(PDF, bottom_left_x, bottom_left_y)
		PDF_lineto(PDF, top_left_x, top_left_y)
		PDF_closepath_fill_stroke(PDF)

	def end_page(self):
		PDF = self.PDF
		PDF_end_page(PDF)	
		
	def close_PDF(self):
		PDF_close(self.PDF)
		PDF_delete(self.PDF)

