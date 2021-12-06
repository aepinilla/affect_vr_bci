using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DefineState : MonoBehaviour
{
    public static string currentValence;
    public static string currentArousal;
    public static string currentState;

    void Update()
    {
        currentValence = ReceiveValenceLabels.ValenceType;
        currentArousal = ReceiveArousalLabels.ArousalType;

        if (currentValence == "hv" && currentArousal == "ha")
        {
            currentState = "exciting";
        }
        else if (currentValence == "hv" && currentArousal == "la")
        {
            currentState = "relaxing";
        }

        else if (currentValence == "lv" && currentArousal == "la")
        {
            currentState = "depressing";
        }

        else if (currentValence == "lv" && currentArousal == "ha")
        {
            currentState = "stressing";
        }

        else
        {
            currentState = "neutral";
        }

    }
}
