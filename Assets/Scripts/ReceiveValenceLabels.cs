using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using LSL;

public class ReceiveValenceLabels : MonoBehaviour
{
    public string streamType = "Control";
    public string streamValenceName = "OutStreamValence";

    public float scaleInput = 0.1f;
    liblsl.StreamInfo[] streamInfosVal;
    liblsl.StreamInlet streamInletVal;
    float[] sample;
    private int channelCount = 0;

    public static string ValenceType;


    void Update()
    {

        if (streamInletVal == null)
        {
            streamInfosVal = liblsl.resolve_stream("name", streamValenceName, 1, 0.0);
            if (streamInfosVal.Length > 0)
            {
                streamInletVal = new liblsl.StreamInlet(streamInfosVal[0]);
                channelCount = streamInletVal.info().channel_count();
                streamInletVal.open_stream();
            }
        }


        if (streamInletVal != null)
        {

            sample = new float[channelCount];
            double lastTimeStamp = streamInletVal.pull_sample(sample, 0.0f);
            if (lastTimeStamp != 0.0)
            {
                if (sample[0] > sample[1])
                {
                    ValenceType = "lv";
                }
                else if (sample[0] < sample[1])
                {
                    ValenceType = "hv";
                }
                else
                {
                    ValenceType = "neutral";
                }
            }
        }
    }
}