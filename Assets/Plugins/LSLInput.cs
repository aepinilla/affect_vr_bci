using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using LSL;

public class LSLInput : MonoBehaviour
{
    public string StreamType = "Control";
    public string StreamName = "OutStream";
    public string ValenceType = "HighValence";
    public float scaleInput = 0.1f;
    liblsl.StreamInfo[] streamInfos;
    liblsl.StreamInlet streamInlet;
    float[] sample;
    private int channelCount = 0;

    void Update()
    {
        
        if (streamInlet == null)
        {
            streamInfos = liblsl.resolve_stream("name", StreamName, 1, 0.0);
            if (streamInfos.Length > 0)
            {
                streamInlet = new liblsl.StreamInlet(streamInfos[0]);
                channelCount = streamInlet.info().channel_count();
                streamInlet.open_stream();
            }
        }

        if (streamInlet != null)
        {
            sample = new float[channelCount];
            double lastTimeStamp = streamInlet.pull_sample(sample, 0.0f);
            
            if (lastTimeStamp != 0.0)
            {
                while ((lastTimeStamp = streamInlet.pull_sample(sample, 0.0f)) != 0)
                {
                    if (sample[0] > sample[1])
                        ValenceType = "Lowalence";
                    else
                        ValenceType = "HighValence";

                    Debug.Log(ValenceType);
                }
            }
        }   
    }
}