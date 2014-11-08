class CreatePublications < ActiveRecord::Migration
  def self.up
    create_table :publications do |t|
      t.string :name
      t.string :url
      t.string :submit_url
      t.boolean :simsub
      t.text :notes
      t.references :submitted_poem_method

      t.timestamps
    end
  end

  def self.down
    drop_table :publications
  end
end
