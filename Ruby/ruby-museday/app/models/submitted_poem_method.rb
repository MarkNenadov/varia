class SubmittedPoemMethod < ActiveRecord::Base
   belongs_to :submitted_poem
   belongs_to :publication
end
