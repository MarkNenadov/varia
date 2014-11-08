class CreateSubmittedPoemStatuses < ActiveRecord::Migration
  def self.up
    create_table :submitted_poem_statuses do |t|
      t.string :name

      t.timestamps
    end
  end

  def self.down
    drop_table :submitted_poem_statuses
  end
end
