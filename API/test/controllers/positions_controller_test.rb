require "test_helper"

class PositionsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @position = positions(:one)
  end

  test "should get index" do
    get positions_url
    assert_response :success
  end

  test "should get new" do
    get new_position_url
    assert_response :success
  end

  test "should create position" do
    assert_difference("Position.count") do
      post positions_url, params: { position: { position_id: @position.position_id, position_name: @position.position_name, salary: @position.salary } }
    end

    assert_redirected_to position_url(Position.last)
  end

  test "should show position" do
    get position_url(@position)
    assert_response :success
  end

  test "should get edit" do
    get edit_position_url(@position)
    assert_response :success
  end

  test "should update position" do
    patch position_url(@position), params: { position: { position_id: @position.position_id, position_name: @position.position_name, salary: @position.salary } }
    assert_redirected_to position_url(@position)
  end

  test "should destroy position" do
    assert_difference("Position.count", -1) do
      delete position_url(@position)
    end

    assert_redirected_to positions_url
  end
end
