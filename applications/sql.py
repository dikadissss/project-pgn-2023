import math

from django.db import connection


def dict_fetchall(cursor):
    """
    Return all rows from a cursor as a dict.
    Assume the column names are unique.
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def list_event(start_time, end_time):
    cursor = connection.cursor()
    cursor.execute(f"select PEvent.publicID AS publicID, \
                                    Origin.time_value AS datetime, \
                                    Origin.evaluationMode AS mode, \
                                    Origin.evaluationStatus AS status, \
                                    Origin.quality_usedPhaseCount AS phase, \
                                    ROUND(Magnitude.magnitude_value,1) AS mag, \
                                    Magnitude.type AS magtype, \
                                    Magnitude.stationCount AS stationCount, \
                                    ROUND(Origin.quality_azimuthalGap) AS azGap, \
                                    ROUND(Origin.quality_standardError,1) AS rms, \
                                    IF(Origin.latitude_value < 0, CONCAT(ABS(ROUND(Origin.latitude_value,2)), ' S'), CONCAT(ABS(ROUND(Origin.latitude_value,2)), ' N')) AS lat, \
                                    ROUND(Origin.latitude_value,2) AS latitude, \
                                    IF(Origin.longitude_value < 0, CONCAT(ABS(ROUND(Origin.longitude_value,2)), ' W'), CONCAT(ABS(ROUND(Origin.longitude_value,2)), ' E')) AS lon, \
                                    ROUND(Origin.longitude_value,2) AS longitude, \
                                    CONCAT(ROUND(Origin.depth_value), ' km') AS depthKm, \
                                    ROUND(Origin.depth_value) AS depth, \
                                    ROUND(FocalMechanism.nodalPlanes_nodalPlane1_strike_value, 0) AS st1, \
                                    ROUND(FocalMechanism.nodalPlanes_nodalPlane1_dip_value, 0) AS d1, \
                                    ROUND(FocalMechanism.nodalPlanes_nodalPlane1_rake_value) AS r1, \
                                    ROUND(FocalMechanism.nodalPlanes_nodalPlane2_strike_value) AS st2, \
                                    ROUND(FocalMechanism.nodalPlanes_nodalPlane2_dip_value) AS d2, \
                                    ROUND(FocalMechanism.nodalPlanes_nodalPlane2_rake_value) AS r2, \
                                    Event.type, \
                                    EventDescription.text AS remark \
    			from Event, PublicObject as PEvent, Origin, PublicObject as POrigin, Magnitude, PublicObject as PMagnitude, FocalMechanism, PublicObject as PFocal, EventDescription \
    			where (Event.type is NULL or Event.type='earthquake') and \
    				Event._oid=PEvent._oid and \
    				Origin._oid=POrigin._oid and \
    				Magnitude._oid=PMagnitude._oid and \
    				PMagnitude.publicID=Event.preferredMagnitudeID and \
                    FocalMechanism._oid = PFocal._oid and \
                    PFocal.publicID = Event.preferredFocalMechanismID and \
    				POrigin.publicID=Event.preferredOriginID and \
    				Event._oid=EventDescription._parent_oid and \
    				EventDescription.type='region name' and \
    				Origin.time_value >= '{start_time}' and Origin.time_value <= '{end_time}' \
                    order by Origin.time_value ASC; ")

    data = dict_fetchall(cursor)
    return data


def list_moment_tensor(start_time, end_time):
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT PEvent.publicID AS publicID, \
            GREATEST(FLOOR(log10(abs(MomentTensor.tensor_Mrr_value))), \
                FLOOR(log10(abs(MomentTensor.tensor_Mtt_value))), \
                FLOOR(log10(abs(MomentTensor.tensor_Mpp_value))), \
                FLOOR(log10(abs(MomentTensor.tensor_Mrt_value))), \
                FLOOR(log10(abs(MomentTensor.tensor_Mrp_value))), \
                FLOOR(log10(abs(MomentTensor.tensor_Mtp_value))), \
                FLOOR(log10(abs(FocalMechanism.principalAxes_tAxis_length_value))), \
                FLOOR(log10(abs(FocalMechanism.principalAxes_nAxis_length_value))), \
                FLOOR(log10(abs(FocalMechanism.principalAxes_pAxis_length_value)))) AS expo, \
            POW(10.0, GREATEST(FLOOR(log10(abs(MomentTensor.tensor_Mrr_value))), \
                FLOOR(log10(abs(MomentTensor.tensor_Mtt_value))), \
                FLOOR(log10(abs(MomentTensor.tensor_Mpp_value))), \
                FLOOR(log10(abs(MomentTensor.tensor_Mrt_value))), \
                FLOOR(log10(abs(MomentTensor.tensor_Mrp_value))), \
                FLOOR(log10(abs(MomentTensor.tensor_Mtp_value))), \
                FLOOR(log10(abs(FocalMechanism.principalAxes_tAxis_length_value))), \
                FLOOR(log10(abs(FocalMechanism.principalAxes_nAxis_length_value))), \
                FLOOR(log10(abs(FocalMechanism.principalAxes_pAxis_length_value))))) AS divided, \
            Origin.time_value AS datetime, \
            Origin.evaluationMode AS mode, \
            Origin.evaluationStatus AS status, \
            Origin.quality_usedPhaseCount AS phase, \
            ROUND(Magnitude.magnitude_value,1) AS mag, \
            Magnitude.type AS magtype, \
            Magnitude.stationCount AS stationCount, \
            ROUND(Origin.quality_azimuthalGap) AS azGap, \
            ROUND(Origin.quality_standardError,1) AS rms, \
            IF(Origin.latitude_value < 0, CONCAT(ABS(ROUND(Origin.latitude_value,2)), ' S'), CONCAT(ABS(ROUND(Origin.latitude_value,2)), ' N')) AS lat, \
            ROUND(Origin.latitude_value,2) AS latitude, \
            IF(Origin.longitude_value < 0, CONCAT(ABS(ROUND(Origin.longitude_value,2)), ' W'), CONCAT(ABS(ROUND(Origin.longitude_value,2)), ' E')) AS lon, \
            ROUND(Origin.longitude_value,2) AS longitude, \
            CONCAT(ROUND(Origin.depth_value), ' km') AS depthKm, \
            ROUND(Origin.depth_value) AS depth, \
            MomentTensor.tensor_Mrr_value AS Mrr, \
            MomentTensor.tensor_Mtt_value AS Mtt, \
            MomentTensor.tensor_Mpp_value AS Mpp, \
            MomentTensor.tensor_Mrt_value AS Mrt, \
            MomentTensor.tensor_Mrp_value AS Mrp, \
            MomentTensor.tensor_Mtp_value AS Mtp, \
            ROUND(FocalMechanism.nodalPlanes_nodalPlane1_strike_value, 0) AS st1, \
            ROUND(FocalMechanism.nodalPlanes_nodalPlane1_dip_value, 0) AS d1, \
            ROUND(FocalMechanism.nodalPlanes_nodalPlane1_rake_value, 0) AS r1, \
            ROUND(FocalMechanism.nodalPlanes_nodalPlane2_strike_value, 0) AS st2, \
            ROUND(FocalMechanism.nodalPlanes_nodalPlane2_dip_value, 0) AS d2, \
            ROUND(FocalMechanism.nodalPlanes_nodalPlane2_rake_value, 0) AS r2, \
            FocalMechanism.principalAxes_tAxis_length_value AS Tval, \
            ROUND(FocalMechanism.principalAxes_tAxis_plunge_value, 0) AS Tplg, \
            ROUND(FocalMechanism.principalAxes_tAxis_azimuth_value, 0) AS Tazi, \
            FocalMechanism.principalAxes_nAxis_length_value AS Nval, \
            ROUND(FocalMechanism.principalAxes_nAxis_plunge_value, 0) AS Nplg, \
            ROUND(FocalMechanism.principalAxes_nAxis_azimuth_value, 0) AS Nazi, \
            FocalMechanism.principalAxes_pAxis_length_value AS Pval, \
            ROUND(FocalMechanism.principalAxes_pAxis_plunge_value, 0) AS Pplg, \
            ROUND(FocalMechanism.principalAxes_pAxis_azimuth_value, 0) AS Pazi, \
            Event.type, \
            EventDescription.text AS remark \
        FROM Event, \
            PublicObject as PEvent, \
            Origin, \
            PublicObject as POrigin, \
            Magnitude, \
            PublicObject as PMagnitude, \
            FocalMechanism, \
            PublicObject as PFocalMechanism, \
            MomentTensor, \
            PublicObject as PMomentTensor, \
            FocalMechanismReference, \
            EventDescription \
        WHERE (Event.type is NULL or Event.type = 'earthquake') AND \
            Event._oid = PEvent._oid AND \
            Origin._oid = POrigin._oid AND \
            Magnitude._oid = PMagnitude._oid AND \
            FocalMechanism._oid = PFocalMechanism._oid AND \
            PFocalMechanism.publicID = Event.preferredFocalMechanismID AND \
            PMagnitude.publicID = Event.preferredMagnitudeID AND \
            POrigin.publicID = Event.preferredOriginID AND \
            Event._oid = EventDescription._parent_oid AND \
            EventDescription.type = 'region name' AND \
            Origin.evaluationMode = 'manual' AND \
            PMomentTensor._oid = MomentTensor._oid AND \
            FocalMechanismReference.focalMechanismID = PFocalMechanism.publicID AND \
            MomentTensor._parent_oid = FocalMechanism._oid AND \
            Origin.time_value >= '{start_time}' AND \
            Origin.time_value <= '{end_time}';"
    )

    data = dict_fetchall(cursor)
    return data
