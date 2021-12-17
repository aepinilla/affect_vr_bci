using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Markers : MonoBehaviour
{
    // Experiment manager
    ExperimentManager experimentManager;
    private string activePhase;

    // Virtual environments
    public GameObject excitingEnvironment;
    public GameObject relaxingEnvironment;
    public GameObject depressingEnvironment;
    public GameObject stressingEnvironment;

    // Markers
    private string Intro        = "intro";
    private string CalibBegin   = "calib-begin";
    private string HighValence  = "hv";
    private string HighArousal  = "ha";
    private string LowValence   = "lv";
    private string LowArousal   = "la";
    private string CalibEnd     = "calib-end";
    private string Baseline     = "baseline";



    private void Start()
    {
        // Call experiment manager
        experimentManager = GameObject.FindGameObjectWithTag("ExperimentManager").GetComponent<ExperimentManager>();
    }


    void Update()
    {
        // Set markers according to active phase
        activePhase = experimentManager.GetCurrentExperimentPhase().ToString();

        if (activePhase == "Intro")
        {
            PlayerPrefs.SetString("MarkerValence", Intro);
            PlayerPrefs.SetString("MarkerArousal", Intro);
        }

        else if (activePhase == "PreCalibration")
        {
            PlayerPrefs.SetString("MarkerValence", CalibBegin);
            PlayerPrefs.SetString("MarkerArousal", CalibBegin);
        }

        else if (activePhase == "Calibration")
        {
            if (excitingEnvironment.activeInHierarchy)
            {
                PlayerPrefs.SetString("MarkerValence", HighValence);
                PlayerPrefs.SetString("MarkerArousal", HighArousal);
            }

            else if (relaxingEnvironment.activeInHierarchy)
            {
                PlayerPrefs.SetString("MarkerValence", HighValence);
                PlayerPrefs.SetString("MarkerArousal", LowArousal);
            }

            else if (depressingEnvironment.activeInHierarchy)
            {
                PlayerPrefs.SetString("MarkerValence", LowValence);
                PlayerPrefs.SetString("MarkerArousal", LowArousal);
            }

            else if (stressingEnvironment.activeInHierarchy)
            {
                PlayerPrefs.SetString("MarkerValence", LowValence);
                PlayerPrefs.SetString("MarkerArousal", HighArousal);
            }

        }

        else if (activePhase == "PostCalibration")
        {
            PlayerPrefs.SetString("MarkerValence", CalibEnd);
            PlayerPrefs.SetString("MarkerArousal", CalibEnd);
        }

        else if (activePhase == "Baseline")
        {
            PlayerPrefs.SetString("MarkerValence", Baseline);
            PlayerPrefs.SetString("MarkerArousal", Baseline);
        }

        
    }
}
