using System.Linq;
using UnityEngine;
using UnityEngine.UI;

public class SwitchScales : MonoBehaviour
{
    public GameObject submitButton;
    public GameObject nextScaleButton;
    public ToggleGroup[] toggleGroups;
    public GameObject[] scales;
    private GameObject currentScale;
    public int scalesIndex = -1;

    public void Present()
    {
        scalesIndex = -1;

        foreach(var toggleGroup in toggleGroups)
        {
            foreach(var toggle in toggleGroup.GetComponentsInChildren<Toggle>(true))
            {
                toggle.isOn = false;
            }
        }

        submitButton.SetActive(false);
        nextScaleButton.SetActive(false);
        scales[0].SetActive(false);
        scales[1].SetActive(false);
        scales[2].SetActive(false);

        this.NextScale();
    }

    public void OnToggleValueChanged()
    {
        if (scalesIndex < 0)
            return;

        if(toggleGroups[scalesIndex].AnyTogglesOn())
        {
            if (scalesIndex < 2)
            {
                nextScaleButton.SetActive(true);
            }
            else
            {
                submitButton.SetActive(true);
            }
        }
        else
        {
            nextScaleButton.SetActive(false);
            submitButton.SetActive(false);
        }

    }

    public void NextScale()
    {
        if (currentScale != null)
        {
            currentScale.SetActive(false);
        }

        if (scalesIndex < 2)
        {
            scalesIndex += 1;
            currentScale = scales[scalesIndex];
            currentScale.SetActive(true);
            nextScaleButton.SetActive(false);
        }
    }
}
