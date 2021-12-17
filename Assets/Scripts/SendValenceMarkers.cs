using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using LSL;
using UnityEngine.SceneManagement;


public class SendValenceMarkers : MonoBehaviour
{
    // Phases
    ExperimentManager experimentManager;
    private string activePhase;
    private string previousPhase = "null";

    // LSL
    private static liblsl.StreamOutlet outlet;
    public string StreamName = "Unity.MarkersValenceStream";
    public string StreamType = "Unity.StreamType";
    public string StreamId = "UnityValence";
    private string[] marker;   

    // Timer
    private float timer = 0.0f;
    private float timeInterval = 1.0f;


    void Start()
    {
        // Call experiment manager
        experimentManager = GameObject.FindGameObjectWithTag("ExperimentManager").GetComponent<ExperimentManager>();

        // LSL
        liblsl.StreamInfo streamInfo = new liblsl.StreamInfo(StreamName, StreamType, 1, liblsl.IRREGULAR_RATE, liblsl.channel_format_t.cf_string);
        liblsl.XMLElement chans = streamInfo.desc().append_child("channels");
        chans.append_child("channel").append_child_value("label", "Marker");
        outlet = new liblsl.StreamOutlet(streamInfo);
        marker = new string[1];
    }


    void Update()
    {
        // Set markers according to active phase
        activePhase = experimentManager.GetCurrentExperimentPhase().ToString();

        if (activePhase == "Intro" || activePhase == "Baseline")
        {
            marker[0] = PlayerPrefs.GetString("MarkerValence");
            activePhase = PlayerPrefs.GetString("CurrentPhase");

            // Send the marker once whenever the experiment phase changes.
            if (activePhase != previousPhase)
            {
                outlet.push_sample(marker);
            }

            previousPhase = activePhase;
        }

        else if (activePhase == "Calibration")
        {
            // Send the marker once per second to Neuropype.
            marker[0] = PlayerPrefs.GetString("MarkerValence");
            timer += Time.deltaTime;

            if (timer > timeInterval)
            {
                outlet.push_sample(marker);
                timer = timer - timeInterval;
            }
        }

        else if (activePhase == "NeuroFeedback")
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