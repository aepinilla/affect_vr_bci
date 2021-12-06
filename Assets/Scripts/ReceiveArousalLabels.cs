using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using LSL;

public class ReceiveArousalLabels : MonoBehaviour
{
    public string streamType = "Control";
    public string streamArousalName = "OutStreamArousal";

    public float scaleInput = 0.1f;
    liblsl.StreamInfo[] streamInfosAr;
    liblsl.StreamInlet streamInletAr;
    float[] sample;
    private int channelCount = 0;

    public static string ArousalType;

    void Update()
    {

        if (streamInletAr == null)
        {
            streamInfosAr = liblsl.resolve_stream("name", streamArousalName, 1, 0.0);
            if (streamInfosAr.Length > 0)
            {
                streamInletAr = new liblsl.StreamInlet(streamInfosAr[0]);
                channelCount = streamInletAr.info().channel_count();
                streamInletAr.open_stream();


            }
        }

        if (streamInletAr != null)
        {
            sample = new float[channelCount];
            double lastTimeStamp = streamInletAr.pull_sample(sample, 0.0f);
            if (lastTimeStamp != 0.0)
            {
                if (sample[0] > sample[1])
                {
                    ArousalType = "ls";
                }
                else if (sample[0] < sample[1])
                {
                    ArousalType = "hs";
                }
                else
                {
                    ArousalType = "neutral";
                }
            }
        }
    }
}