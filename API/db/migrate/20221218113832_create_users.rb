class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :login
      t.string :first_name
      t.string :last_name
      t.string :account_type
      t.string :email
      t.string :account_no

      t.timestamps
    end
  end
end
