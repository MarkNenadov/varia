class CreatePoems < ActiveRecord::Migration
  def self.up
    create_table :poems do |t|
      t.string :title
      t.text :content
      t.text :notes

      t.timestamps
    end
  end

  def self.down
    drop_table :poems
  end
end
