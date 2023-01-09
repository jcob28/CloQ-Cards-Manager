class AddIndexToUsersIndex < ActiveRecord::Migration[7.0]
  def change
    add_index :users, :user_index, unique: true
  end
end
