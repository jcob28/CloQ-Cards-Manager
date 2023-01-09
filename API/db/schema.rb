# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.0].define(version: 2022_12_27_151127) do
  create_table "employees", force: :cascade do |t|
    t.integer "user_id", null: false
    t.string "department"
    t.integer "manager_id", null: false
    t.integer "position_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["manager_id"], name: "index_employees_on_manager_id"
    t.index ["position_id"], name: "index_employees_on_position_id"
    t.index ["user_id"], name: "index_employees_on_user_id"
  end

  create_table "gates", force: :cascade do |t|
    t.integer "user_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["user_id"], name: "index_gates_on_user_id"
  end

  create_table "managers", force: :cascade do |t|
    t.integer "user_id", null: false
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["user_id"], name: "index_managers_on_user_id"
  end

  create_table "positions", force: :cascade do |t|
    t.string "position_name"
    t.integer "salary"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "registers", force: :cascade do |t|
    t.integer "employee_id", null: false
    t.integer "gate"
    t.date "date_in"
    t.time "time_in"
    t.date "date_out"
    t.time "time_out"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["employee_id"], name: "index_registers_on_employee_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "login"
    t.string "first_name"
    t.string "last_name"
    t.string "account_type"
    t.string "email"
    t.string "account_no"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "password_digest"
    t.index ["login"], name: "index_users_on_login", unique: true
  end

  create_table "vacations", force: :cascade do |t|
    t.integer "employee_id", null: false
    t.date "start_date"
    t.date "end_date"
    t.string "vacation_type"
    t.boolean "decision"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["employee_id"], name: "index_vacations_on_employee_id"
  end

  add_foreign_key "employees", "managers"
  add_foreign_key "employees", "positions"
  add_foreign_key "employees", "users"
  add_foreign_key "gates", "users"
  add_foreign_key "managers", "users"
  add_foreign_key "registers", "employees"
  add_foreign_key "vacations", "employees"
end
