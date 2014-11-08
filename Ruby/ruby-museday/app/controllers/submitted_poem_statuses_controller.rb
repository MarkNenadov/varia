class SubmittedPoemStatusesController < ApplicationController
   def new
      @submitted_poem_status = SubmittedPoemStatus.new
   end

   def create
      @submitted_poem_status = SubmittedPoemStatus.new(:name => params[:submitted_poem_status][:name])
      if @submitted_poem_status.save
        redirect_to @submitted_poem_status
      else
        render 'new'
      end
   end

   def show
      @submitted_poem_status = SubmittedPoemStatus.find(params[:id])
   end

   def index
      @submitted_poem_statuses = SubmittedPoemStatus.all
   end

   def edit
      @poem = SubmittedPoemStatuses.find(params[:id])
   end

   def update
      @submitted_poem_status = SubmittedPoemStatuses.find(params[:id])

      if @submitted_poem_status.update(params[:poem].permit(:name))
         redirect_to @submitted_poem_status
      else
         render 'edit'
      end
   end

end
