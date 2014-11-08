class PublicationsController < ApplicationController
   def new
      @publication = Publication.new
   end

   def create
      @publication = Publication.new(:name => params[:publication][:name], 
                                     :url => params[:publication][:url], 
                                     :simsub => params[:publication][:simsub],
                                     :notes => params[:notes])
      if @publication.save
        redirect_to @publication
      else
        render 'new'
      end
   end

   def index
      @publications = Publication.all
   end

   def show
      @publication = Publication.find(params[:id])
   end

   def edit
      @publication = Publication.find(params[:id])
   end

   def update
      @publication = Publciation.find(params[:id])

      if (@publication.update(params[:publication].permit(:name,:url,:simsub,:notes)))
         redirect_to @publication
      else
         render 'edit'
      end
   end
   
   private
      def publication_params
         params.require(:publication).permit(:name, :url, :simsub, :notes)
      end

end
