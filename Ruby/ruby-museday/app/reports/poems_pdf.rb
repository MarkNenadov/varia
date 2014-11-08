require "prawn"

class PoemPdf < Prawn::Document
   def initialize(poem, view)
      super()
      @poem = poem
      @view = view
      title
   end

   def title
      font_style = :bold
      text @poem.title
      move_down 15
      text @poem.content
   end
end
