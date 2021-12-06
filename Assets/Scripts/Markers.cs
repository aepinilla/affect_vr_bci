using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Markers : MonoBehaviour
{
    // Virtual environments
    public GameObject excitingEnvironment;
    public GameObject relaxingEnvironment;
    public GameObject depressingEnvironment;
    public GameObject stressingEnvironment;

    // Markers
    private string CalibBegin        = "calib-begin";
    private string HighValence       = "hv";
    private string HighArousal       = "ha";
    private string LowValence        = "lv";
    private string LowArousal        = "la";
    private string CalibEnd          = "calib-end";


    void Update()
    {
        if (/*calibration phase started*/)
        {
            PlayerPrefs.SetString("MarkerValence", CalibBegin);
            PlayerPrefs.SetString("MarkerArousal", CalibBegin);
        }

        else if (/*calibration phase over*/)
        {
            PlayerPrefs.SetString("MarkerValence", CalibEnd);
            PlayerPrefs.SetString("MarkerArousal", CalibEnd);
        }

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
}
