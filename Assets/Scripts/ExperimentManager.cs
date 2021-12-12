using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

public class ExperimentManager : MonoBehaviour
{
    public SelfAssessmentManikin selfAssessmentManikin;
    public GameObject finishScreen;

    public GameObject excitingEnvironment;
    public GameObject relaxingEnvironment;
    public GameObject depressingEnvironment;
    public GameObject stressingEnvironment;

    private int trialIndex = -1;

    public float repetitionDuration = 60;

    public TrialDefinition[] calibrationTrials;
    public TrialDefinition[] baselineTrials;
    public TrialDefinition[] neuroFeedbackTrials;

    private GameObject[] trials;

    private void Start()
    {
        var trialsList = new List<GameObject>();
        var trialDefinitions = calibrationTrials.Concat(baselineTrials).Concat(neuroFeedbackTrials);
        foreach(var trialDefinition in trialDefinitions)
        {
            for(int i = 0; i < trialDefinition.repetitions; i++)
            {
                var environment = trialDefinition.trialType switch
                {
                    TrialType.Exciting => excitingEnvironment,
                    TrialType.Relaxing => relaxingEnvironment,
                    TrialType.Depressing => depressingEnvironment,
                    TrialType.Stressing => stressingEnvironment,
                    TrialType.Random => GetRandomEnvironment(),
                    _ => GetRandomEnvironment(),
                };
                trialsList.Add(environment);
            }
        }
        this.trials = trialsList.ToArray();
    }

    public ExperimentPhase GetCurrentExperimentPhase()
    {
        if (trialIndex < calibrationTrials.Length)
            return ExperimentPhase.Calibration;
        else if (trialIndex < (calibrationTrials.Length + baselineTrials.Length))
            return ExperimentPhase.Baseline;
        else
            return ExperimentPhase.NeuroFeedback;
    }

    private GameObject GetRandomEnvironment() => new[]{
            excitingEnvironment,
            relaxingEnvironment,
            depressingEnvironment,
            stressingEnvironment
        }[Random.Range(0, 4)];



    public void ContinueExperiment()
    {
        trialIndex++;
        if (trialIndex < trials.Length)
        {
            StartCoroutine(Present(trials[trialIndex]));
        }
        else
        {
            finishScreen.SetActive(true);
        }
    }

    public IEnumerator Present(GameObject environment)
    {
        environment.SetActive(true);
        yield return new WaitForSeconds(repetitionDuration);
        environment.SetActive(false);
        selfAssessmentManikin.gameObject.SetActive(true);
        selfAssessmentManikin.Present();
    }
}
