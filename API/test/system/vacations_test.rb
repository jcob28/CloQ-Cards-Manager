require "application_system_test_case"

class VacationsTest < ApplicationSystemTestCase
  setup do
    @vacation = vacations(:one)
  end

  test "visiting the index" do
    visit vacations_url
    assert_selector "h1", text: "Vacations"
  end

  test "should create vacation" do
    visit vacations_url
    click_on "New vacation"

    check "Decision" if @vacation.decision
    fill_in "Employee", with: @vacation.employee_id
    fill_in "End date", with: @vacation.end_date
    fill_in "Start date", with: @vacation.start_date
    fill_in "Vacation", with: @vacation.vacation_id
    fill_in "Vacation type", with: @vacation.vacation_type
    click_on "Create Vacation"

    assert_text "Vacation was successfully created"
    click_on "Back"
  end

  test "should update Vacation" do
    visit vacation_url(@vacation)
    click_on "Edit this vacation", match: :first

    check "Decision" if @vacation.decision
    fill_in "Employee", with: @vacation.employee_id
    fill_in "End date", with: @vacation.end_date
    fill_in "Start date", with: @vacation.start_date
    fill_in "Vacation", with: @vacation.vacation_id
    fill_in "Vacation type", with: @vacation.vacation_type
    click_on "Update Vacation"

    assert_text "Vacation was successfully updated"
    click_on "Back"
  end

  test "should destroy Vacation" do
    visit vacation_url(@vacation)
    click_on "Destroy this vacation", match: :first

    assert_text "Vacation was successfully destroyed"
  end
end
