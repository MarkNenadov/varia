class SubmissionsController < ApplicationController
   def new
      @submission = Submission.new
   end

   def create
      submission_date = Date.civil(params["date(1i)"].to_i, params["date(2i)"].to_i, params["date(3i)"].to_i)
      followup_date = Date.civil(params["followup_date(1i)"].to_i, params["followup_date(2i)"].to_i, params["followup_date(3i)"].to_i)
      @submission=Submission.new(:date => submission_date, 
                                 :followup_date => followup_date, 
                                 :notes => params[:submission][:notes])

      if @submission.save
        redirect_to @submission
      else
        render 'new'
      end
   end

   def show
      @submission = Submission.find(params[:id])
   end

   def index
      @submissions = Submission.all
   end

   def edit
      @submission = Submission.find(params[:id])
   end

   def update
      @submission = Submission.find(params[:id])

      if @submission.update(params[:submission].permit(:date, :followup_date, :notes ))
         redirect_to @submission
      else
         render 'edit'
      end
   end

   private
      def submission_params
         params.require(:submission).permit(:date, :followup_date, :notes)
      end
end
