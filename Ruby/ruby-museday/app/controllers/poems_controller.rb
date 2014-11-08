require "prawn"
require "poems_pdf"

class PoemsController < ApplicationController
   def new
      @poem = Poem.new
   end

   def create
      @poem = Poem.new(:title => params[:poem][:title], :content => params[:poem][:content], :notes => params[:poem][:notes])
      if @poem.save
        redirect_to @poem
      else
        render 'new'
      end
   end

   def show
      @poem = Poem.find(params[:id])
      respond_to do |format|
         format.html
         format.pdf do
            pdf = PoemPdf.new(@poem, view_context)
            send_data pdf.render, filename: "test.pdf", type: "application/pdf"         
         end
      end
   end

   def index
      @poems = Poem.all
   end

   def edit
      @poem = Poem.find(params[:id])
   end

   def update
      @poem = Poem.find(params[:id])

      if @poem.update(params[:poem].permit(:title,:content,:notes))
         redirect_to @poem
      else
         render 'edit'
      end
   end

   private
      def poem_params
         params.require(:poem).permit(:title, :content, :notes)
      end
end
