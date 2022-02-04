using UnityEngine;
using UnityEngine.Events;
using UnityEngine.UI;

public class SelfAssessmentManikin : MonoBehaviour
{
    public SwitchScales switchScales;
    public UnityEvent onSubmit = new UnityEvent();

    public void Present()
    {
        switchScales.Present();
    }

    public void SubmitAnswers()
    {
        this.onSubmit.Invoke();
        this.gameObject.SetActive(false);
    }
}
