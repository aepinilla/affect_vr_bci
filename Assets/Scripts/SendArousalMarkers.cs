using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using LSL;
using UnityEngine.SceneManagement;


public class SendArousalMarkers : MonoBehaviour
{
    private static liblsl.StreamOutlet outlet;
    public string StreamName = "Unity.MarkersArousalStream";
    public string StreamType = "Unity.StreamType";
    public string StreamId = "UnityArousal";
    private string[] marker;
    private string currentPhase;
    private string previousPhase = "null";

    private int i = 0;

    private float timer = 0.0f;
    private float timeInterval = 1.0f;


    void Start()
    {
        liblsl.StreamInfo streamInfo = new liblsl.StreamInfo(StreamName, StreamType, 1, liblsl.IRREGULAR_RATE, liblsl.channel_format_t.cf_string);
        liblsl.XMLElement chans = streamInfo.desc().append_child("channels");
        chans.append_child("channel").append_child_value("label", "Marker");
        outlet = new liblsl.StreamOutlet(streamInfo);
        marker = new string[1];
    }


    void Update()
    {
        /* if (calibration phase has not started) */
        {
            marker[0] = PlayerPrefs.GetString("MarkerArousal");
            activeObject = PlayerPrefs.GetString("ActiveObject");

            // Send the marker once whenever the experiment phase changes.
            if (currentPhase != previousPhase)
            {
                outlet.push_sample(marker);
            }

            previousPhase = currentPhase;
        }

        /* if (calibration phase is active) */
        {
            // Send the marker once per second to Neuropype.
            marker[0] = PlayerPrefs.GetString("MarkerArousal");
            timer += Time.deltaTime;

            if (timer > timeInterval)
            {
                outlet.push_sample(marker);
                timer = timer - timeInterval;
            }
        }

        /*else if (calibration phase is over) */
        {
            // Send an "unkown" marker once per second.
            // This is necessary to get a "reply" back from Neuropype with the output of the classifier.
            marker[0] = "unknown";
            timer += Time.deltaTime;
            if (timer > timeInterval)
            {
                outlet.push_sample(marker);
                timer = timer - timeInterval;
            }
        }
    }
}