class CreateVacations < ActiveRecord::Migration[7.0]
  def change
    create_table :vacations do |t|
      t.references :employee, null: false, foreign_key: true
      t.date :start_date
      t.date :end_date
      t.string :vacation_type
      t.boolean :decision

      t.timestamps
    end
  end
end
