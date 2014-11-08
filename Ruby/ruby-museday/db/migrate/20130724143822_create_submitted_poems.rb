class CreateSubmittedPoems < ActiveRecord::Migration
  def self.up
    create_table :submitted_poems do |t|
      t.references :poem
      t.string :name
      t.date :date
      t.references :submitted_poem_method

      t.timestamps
    end
  end

  def self.down
    drop_table :submitted_poems
  end
end
