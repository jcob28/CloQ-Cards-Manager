require "test_helper"

class GatesControllerTest < ActionDispatch::IntegrationTest
  setup do
    @gate = gates(:one)
  end

  test "should get index" do
    get gates_url
    assert_response :success
  end

  test "should get new" do
    get new_gate_url
    assert_response :success
  end

  test "should create gate" do
    assert_difference("Gate.count") do
      post gates_url, params: { gate: { gate_id: @gate.gate_id, user_id: @gate.user_id } }
    end

    assert_redirected_to gate_url(Gate.last)
  end

  test "should show gate" do
    get gate_url(@gate)
    assert_response :success
  end

  test "should get edit" do
    get edit_gate_url(@gate)
    assert_response :success
  end

  test "should update gate" do
    patch gate_url(@gate), params: { gate: { gate_id: @gate.gate_id, user_id: @gate.user_id } }
    assert_redirected_to gate_url(@gate)
  end

  test "should destroy gate" do
    assert_difference("Gate.count", -1) do
      delete gate_url(@gate)
    end

    assert_redirected_to gates_url
  end
end
