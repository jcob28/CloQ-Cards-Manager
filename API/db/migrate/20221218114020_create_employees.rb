class CreateEmployees < ActiveRecord::Migration[7.0]
  def change
    create_table :employees do |t|
      t.references :user, null: false, foreign_key: true
      t.string :department
      t.references :manager, null: false, foreign_key: true
      t.references :position, null: false, foreign_key: true

      t.timestamps
    end
  end
end
