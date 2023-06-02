from shoulder import BiomechCoordinateSystem, Joint, CartesianAxis, JointType, EulerSequence, check_biomech_consistency


def test_checks():
    # A very standard example of the sterno-clavicular joint, already in ISB
    print(" -- Sterno-clavicular joint -- ISB")
    thorax = BiomechCoordinateSystem(
        antero_posterior_axis=CartesianAxis.plusX,
        infero_superior_axis=CartesianAxis.plusY,
        medio_lateral_axis=CartesianAxis.plusZ,
    )
    assert thorax.is_isb() == True
    clavicle = BiomechCoordinateSystem(
        antero_posterior_axis=CartesianAxis.plusX,
        infero_superior_axis=CartesianAxis.plusY,
        medio_lateral_axis=CartesianAxis.plusZ,
    )
    assert clavicle.is_isb() == True
    sterno_clav = Joint(
        joint_type=JointType.STERNO_CLAVICULAR,
        euler_sequence=EulerSequence.YXZ,
    )
    print(sterno_clav.is_joint_sequence_isb())
    assert sterno_clav.is_joint_sequence_isb() == True
    output = check_biomech_consistency(
        parent_segment=thorax,
        child_segment=clavicle,
        joint=sterno_clav,
    )
    print(output)  # (True, (1, 1, 1))
    assert output[0] == True
    assert output[1] == (1, 1, 1)

    # A not standard example of the sterno-clavicular joint, not in ISB
    print(" -- Sterno-clavicular joint -- not ISB")
    thorax = BiomechCoordinateSystem(
        antero_posterior_axis=CartesianAxis.plusX,
        infero_superior_axis=CartesianAxis.plusY,
        medio_lateral_axis=CartesianAxis.plusZ,
    )
    print(thorax.is_isb())
    assert thorax.is_isb() == True
    clavicle = BiomechCoordinateSystem(
        antero_posterior_axis=CartesianAxis.minusY,
        infero_superior_axis=CartesianAxis.plusX,
        medio_lateral_axis=CartesianAxis.plusZ,
    )
    print(clavicle.is_isb())
    assert clavicle.is_isb() == False
    sterno_clav = Joint(
        joint_type=JointType.STERNO_CLAVICULAR,
        euler_sequence=EulerSequence.YXZ,
    )
    print(sterno_clav.is_joint_sequence_isb())
    assert sterno_clav.is_joint_sequence_isb() == True

    output = check_biomech_consistency(
        parent_segment=thorax,
        child_segment=clavicle,
        joint=sterno_clav,
    )
    # todo: test this output

    # A not standard example of the sterno-clavicular joint, not in ISB, but compatible with ISB
    print(" -- Sterno-clavicular joint -- not ISB but compatible")
    thorax = BiomechCoordinateSystem(
        antero_posterior_axis=CartesianAxis.plusX,
        infero_superior_axis=CartesianAxis.plusZ,
        medio_lateral_axis=CartesianAxis.minusY,
    )
    print(thorax.is_isb())
    assert thorax.is_isb() == False
    clavicle = BiomechCoordinateSystem(
        antero_posterior_axis=CartesianAxis.plusX,
        infero_superior_axis=CartesianAxis.plusZ,
        medio_lateral_axis=CartesianAxis.minusY,
    )
    assert clavicle.is_isb() == False
    print(clavicle.is_isb())
    sterno_clav = Joint(
        joint_type=JointType.STERNO_CLAVICULAR,
        euler_sequence=EulerSequence.ZXY,
    )
    print(sterno_clav.is_joint_sequence_isb())
    assert sterno_clav.is_joint_sequence_isb() == False

    output = check_biomech_consistency(
        parent_segment=thorax,
        child_segment=clavicle,
        joint=sterno_clav,
    )
    # (True, (1, 1, -1))
    print(output)
    assert output[0] == True
    assert output[1] == (1, 1, -1)