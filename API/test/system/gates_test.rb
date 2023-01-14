require "application_system_test_case"

class GatesTest < ApplicationSystemTestCase
  setup do
    @gate = gates(:one)
  end

  test "visiting the index" do
    visit gates_url
    assert_selector "h1", text: "Gates"
  end

  test "should create gate" do
    visit gates_url
    click_on "New gate"

    fill_in "Gate", with: @gate.gate_id
    fill_in "User", with: @gate.user_id
    click_on "Create Gate"

    assert_text "Gate was successfully created"
    click_on "Back"
  end

  test "should update Gate" do
    visit gate_url(@gate)
    click_on "Edit this gate", match: :first

    fill_in "Gate", with: @gate.gate_id
    fill_in "User", with: @gate.user_id
    click_on "Update Gate"

    assert_text "Gate was successfully updated"
    click_on "Back"
  end

  test "should destroy Gate" do
    visit gate_url(@gate)
    click_on "Destroy this gate", match: :first

    assert_text "Gate was successfully destroyed"
  end
end
