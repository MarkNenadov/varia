class CreateSubmissions < ActiveRecord::Migration
  def self.up
    create_table :submissions do |t|
      t.date :date
      t.date :followup_date
      t.string :notes
      t.references :submitted_poem

      t.timestamps
    end
  end

  def self.down
    drop_table :submissions
  end
end
