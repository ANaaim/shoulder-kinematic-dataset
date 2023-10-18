from .utils import TestUtils


def test_first_example():
    spartacus = TestUtils.spartacus_folder()
    module = TestUtils.load_module(spartacus + "/examples/first_example.py")
    confident_values = module.main()

    # verify the number of unique articles
    articles = list(confident_values["article"].unique())
    assert len(articles) == 9

    # Verify that the dataframe has the correct data
    Bourne2003 = confident_values[confident_values["article"] == "Bourne 2003"]
    assert Bourne2003.shape[0] == 2550
    humeral_motions = list(Bourne2003["humeral_motion"].unique())
    assert "frontal elevation" in humeral_motions
    assert "horizontal flexion" in humeral_motions

    joints = list(Bourne2003["joint"].unique())
    assert "scapulothoracic" in joints

    dofs = list(Bourne2003["degree_of_freedom"].unique())
    assert "1" in dofs
    assert "2" in dofs
    assert "3" in dofs

    # test three random values in the value columns and start and end
    assert Bourne2003["value"].iloc[0] == -16.3663
    assert Bourne2003["value"].iloc[1001] == 22.2405
    assert Bourne2003["value"].iloc[2000] == -38.2519
    assert Bourne2003["value"].iloc[-1] == 17.785