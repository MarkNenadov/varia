class CreateSubmittedPoemMethods < ActiveRecord::Migration
  def self.up
    create_table :submitted_poem_methods do |t|
      t.string :name
      t.string :short_code

      t.timestamps
    end
  end

  def self.down
    drop_table :submitted_poem_methods
  end
end
