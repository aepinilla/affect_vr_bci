<?xml version='1.0' encoding='utf-8'?>
<scheme description="This artifact removal pipeline can remove some of the common artifacts in bio-signals such as eye movements, blinks, cardiac signals, muscle artifacts, bad channels, and so on. This pipeline requires initial calibration data whose length can be set as via a parameter. The calibration is required as a baseline for the various artifact removal stages.&#10;&#10;Description of processing nodes:&#10;&#10;- LSL input: is used to input the streamed data into the pipeline.&#10;&#10;- Select range: is used to select desired segments of signal. For example if certain channels does not include meaningful EEG data we can exclude them from the data stream.&#10;&#10;tunable parameter:&#10;1. select_axis: indicates the axis to be used for data section.&#10;2. select_range: indicates the selection range along the chosen axis.&#10;&#10;- Assign Channel Locations: is used to assign channel coordinates, this node is essential to be placed before “Bad channel removal” node.&#10;&#10;- IIR filter:  is used to highpass filter the data. The preceding nodes, Bad channel removal, Channel repair filter and Artifact removal, all require that the data is high passed to ensure that the drift has been removed.&#10;&#10;tunable parameter:&#10;1. stopband edge freq.: indicates the stop-band edge frequency for the highness filter, frequencies below this value will be attenuated by default by 60dB.&#10;2. passband edge freq: indicates the pass-band edge frequency for the highness filter, frequencies above this value will pass with no attenuation.&#10;&#10;- Bad Channel Removal: is used to remove channels with abnormal data from a continuous EEG signal, which ensures that the data contains no channels that record only noise for extended periods of time.&#10;&#10;tunable parameters:&#10;1.  correlation threshold : Correlation threshold between 0 and  1. Higher values (above 0.7) are more stringent and will remove more  channels (i.e., moderately bad channels get removed). Values below 0.6 would be considered very lax (i.e., only the worst channels get removed). &#10;2.  noise threshold : High-frequency noise threshold is measured in multiple of standards deviations. Lower values (below 3.5) are more stringent and will remove more channels (i.e., moderately bad channels will get removed). Values above 5 would be considered very lax (i.e., only the worst channels get removed). &#10;&#10;- Channel Repair Filter: is used to identify and repair segments during which a channel yields bad data.&#10;&#10;tunable parameters:&#10;1. min_corr: Correlation threshold between 0 and 1. Higher values (above 0.7) are more aggressive and will cause channels to be repaired even when they have only moderate artifacts. Values below 0.5 would be considered rather lax (i.e., only the worst channel artifacts get repaired). &#10;2. processing-delay  : Signal delay in seconds. If this is value is set to too low values some sharp-onset artifacts will leave brief  knacks in the data.&quot;&#10;&#10;- Artifact Removal : is used to remove various kinds of high-amplitude artifacts from the signal. Artifacts are identified based on a threshold, given in standard deviations relative to (fairly) clean calibration data. This filter will work best on signals with multiple correlated channels, such as EEG or MEG. &#10;&#10;tunable parameters:&#10;1.  cutoff:  indicates the threshold for artifact removal, measured in multiples of standard deviations. Data portions whose amplitude is larger than this threshold (relative to the calibration data) are considered bad data and will be removed. The most aggressive value that can be used without losing too much EEG is  2.5. A quite conservative value would be 5.0&#10;2. lookahead : indicates the delay in output signal in seconds, can be between 0 (no lookahead) and  WindowLength/2 (optimal lookahead). The default value is set to  window_length/2.&#10;3. max_dims : indicates the maximum dimensionality of artifacts to remove can be a value between 0.1 to 1.0. Up to this many dimensions (or up to this fraction of dimensions) can be removed for a given data segment. If the algorithm needs to tolerate extreme artifacts a higher value than the default may be used, the default is set to  0.66." title="ValencePipeline" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(-679.0, 108.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="50d432c0-d68e-44bc-8140-70f0dd1cc2a7" version="1.0.0" />
		<node id="1" name="Bad Channel Removal" position="(-150.0, 113.0)" project_name="NeuroPype" qualified_name="widgets.neural.owbadchannelremoval.OWBadChannelRemoval" title="Bad Channel Removal" uuid="bd0272f3-e228-44a9-9fe1-c898e6572683" version="1.1.0" />
		<node id="2" name="Assign Channel Locations" position="(-360.0, 106.0)" project_name="NeuroPype" qualified_name="widgets.source_localization.owassignchannellocations.OWAssignChannelLocations" title="Assign Channel Locations" uuid="01bebb1b-cef2-4d9e-b8c8-32fa4e4b5d6f" version="1.0.0" />
		<node id="3" name="Interpolate Missing Channels" position="(106.0, 106.0)" project_name="NeuroPype" qualified_name="widgets.neural.owinterpolatemissingchannels.OWInterpolateMissingChannels" title="Interpolate Missing Channels" uuid="056423f0-575d-4ef1-bedb-a02fa832a0dc" version="0.9.0" />
		<node id="4" name="Remove Unlocalized Channels" position="(-260.0, 106.0)" project_name="NeuroPype" qualified_name="widgets.source_localization.owremoveunlocalizedchannels.OWRemoveUnlocalizedChannels" title="Remove Unlocalized Channels" uuid="8e17eb3c-de80-4261-8443-f253d9a2558a" version="1.0.0" />
		<node id="5" name="Extract Channel Names" position="(-94.0, 6.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owextractchannels.OWExtractChannels" title="Extract Channel Names" uuid="1054dfee-ed1e-4d2f-8e7d-aa0bbd6b6617" version="1.0.0" />
		<node id="6" name="Artifact Removal" position="(-29.0, 112.0)" project_name="NeuroPype" qualified_name="widgets.neural.owartifactremoval.OWArtifactRemoval" title="Artifact Removal" uuid="fefdee9c-cde4-4d68-b164-3a530915062e" version="2.0.0" />
		<node id="7" name="Dejitter Timestamps" position="(-566.0, 108.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="e43a03f8-136c-4da8-9364-23e295de2bbc" version="1.0.0" />
		<node id="8" name="FIR Filter" position="(-545.0, 324.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="Bandpass Filter" uuid="366ee6b1-a306-456c-be81-879f8b98d7e2" version="1.0.0" />
		<node id="9" name="Divide" position="(171.0, 335.0)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owdivide.OWDivide" title="F7 Theta Power Ratio" uuid="37876cce-0aa1-428f-a1df-fa5351fff73c" version="1.0.0" />
		<node id="10" name="Subtract" position="(316.0, 466.0)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owsubtract.OWSubtract" title="Theta Frontal Asymmetry" uuid="2c0fa673-affe-4cd7-8972-1692479836f4" version="1.0.0" />
		<node id="11" name="Segmentation" position="(-182.0, 322.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation Valence" uuid="a84794c4-eb38-46b6-b7b3-263ef2ace0ce" version="1.0.1" />
		<node id="12" name="Assign Target Values" position="(-291.0, 323.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Target Values Valence" uuid="1799947c-66e9-4e80-8fca-415af56092b5" version="1.0.0" />
		<node id="13" name="Logistic Regression" position="(450.0, 467.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlogisticregression.OWLogisticRegression" title="Logistic Regression  Valence" uuid="2d686216-9b48-4919-82d7-a4757cbce1c4" version="1.0.0" />
		<node id="14" name="LSL Output" position="(569.0, 459.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output Valence" uuid="9b2f1831-a6b2-43fc-94e7-5752593a390c" version="1.0.0" />
		<node id="15" name="Print To Console" position="(574.0, 595.0)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owprinttoconsole.OWPrintToConsole" title="Print To Console Valence" uuid="437d0805-5ffd-4215-9877-b0c13322fdb3" version="1.0.0" />
		<node id="16" name="Accumulate Calibration Data" position="(-402.0, 322.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owaccumulatecalibrationdata.OWAccumulateCalibrationData" title="Accumulate Calibration Data Valence" uuid="82d8de18-5413-4fbb-aad0-f710d3ab496e" version="1.0.0" />
		<node id="17" name="Select Range" position="(-72.0, 313.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="F7" uuid="e3a56515-93a8-421d-b544-d8f0117a477c" version="1.0.0" />
		<node id="18" name="Select Range" position="(-55.0, 536.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="F8" uuid="58dd848c-cbf6-4952-aa13-dd8e6453fa3e" version="1.0.0" />
		<node id="19" name="Divide" position="(173.0, 592.0)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owdivide.OWDivide" title="F8 Theta Power Ratio" uuid="0fcddcfe-2a59-45d5-b2c8-02e338baa06a" version="1.0.0" />
		<node id="20" name="FFT Band-Pass Filter" position="(49.0, 305.0)" project_name="NeuroPype" qualified_name="widgets.spectral.owspectralselection.OWSpectralSelection" title="Theta Power F7" uuid="587fc307-884d-47d4-a03b-50910a40daa5" version="1.0.0" />
		<node id="21" name="FFT Band-Pass Filter" position="(50.0, 409.0)" project_name="NeuroPype" qualified_name="widgets.spectral.owspectralselection.OWSpectralSelection" title="Total Power F7" uuid="18a2c30a-9aa8-4cc4-bbe8-46560d7583bf" version="1.0.0" />
		<node id="22" name="FFT Band-Pass Filter" position="(42.0, 527.0)" project_name="NeuroPype" qualified_name="widgets.spectral.owspectralselection.OWSpectralSelection" title="Theta Power F8" uuid="415923fd-7a22-48b6-8e43-4d7ba7e4659e" version="1.0.0" />
		<node id="23" name="FFT Band-Pass Filter" position="(39.0, 617.0)" project_name="NeuroPype" qualified_name="widgets.spectral.owspectralselection.OWSpectralSelection" title="Total Power F8" uuid="4bfba898-dee2-464b-977b-60d395a22d46" version="1.0.0" />
		<node id="24" name="IIR Filter" position="(-468.0, 110.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" title="HighPass &amp; Notch Filter" uuid="5c0ef7fa-29f6-4a63-88ab-e15250fbc5e0" version="1.1.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Desired Channels" sink_node_id="3" source_channel="Channel Names" source_node_id="5" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="12" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="18" source_channel="Data" source_node_id="11" />
		<link enabled="true" id="9" sink_channel="Data1" sink_node_id="10" source_channel="Outdata" source_node_id="9" />
		<link enabled="true" id="10" sink_channel="Data2" sink_node_id="10" source_channel="Outdata" source_node_id="19" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="20" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="21" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="14" sink_channel="Data1" sink_node_id="9" source_channel="Data" source_node_id="20" />
		<link enabled="true" id="15" sink_channel="Data2" sink_node_id="9" source_channel="Data" source_node_id="21" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="22" source_channel="Data" source_node_id="18" />
		<link enabled="true" id="17" sink_channel="Data" sink_node_id="23" source_channel="Data" source_node_id="18" />
		<link enabled="true" id="18" sink_channel="Data1" sink_node_id="19" source_channel="Data" source_node_id="22" />
		<link enabled="true" id="19" sink_channel="Data2" sink_node_id="19" source_channel="Data" source_node_id="23" />
		<link enabled="true" id="20" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="21" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="24" />
		<link enabled="true" id="22" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="23" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="24" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="25" sink_channel="Data" sink_node_id="24" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="26" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="27" sink_channel="Data" sink_node_id="13" source_channel="Outdata" source_node_id="10" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFghAAAAbmFtZT0nVW5pdHkuTWFya2Vyc1ZhbGVuY2VTdHJlYW0ncQVYDAAAAG1h
eF9ibG9ja2xlbnEGTQAEWAoAAABtYXhfYnVmbGVucQdLHlgMAAAAbWF4X2NodW5rbGVucQhLAFgM
AAAAbm9taW5hbF9yYXRlcQlYDQAAACh1c2UgZGVmYXVsdClxClgFAAAAcXVlcnlxC1gKAAAAbmFt
ZT0nRUVHJ3EMWAcAAAByZWNvdmVycQ2IWBQAAAByZXNvbHZlX21pbmltdW1fdGltZXEORz/gAAAA
AAAAWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91bnBpY2tsZV90eXBlCnEQWAwAAABQ
eVF0NC5RdENvcmVxEVgKAAAAUUJ5dGVBcnJheXESQy4B2dDLAAEAAAAAAg4AAAFTAAADhQAAAskA
AAIWAAABcgAAA30AAALBAAAAAAAAcROFcRSHcRVScRZYDgAAAHNldF9icmVha3BvaW50cReJdS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWA0AAABjYWxpYl9zZWNvbmRzcQFLD1gPAAAAY29vcmRzX292ZXJyaWRlcQJYDQAAACh1
c2UgZGVmYXVsdClxA1gOAAAAY29ycl90aHJlc2hvbGRxBEc/6ZmZmZmZmlgPAAAAaWdub3JlX2No
YW5sb2NzcQWJWBAAAABpZ25vcmVkX3F1YW50aWxlcQZHP7mZmZmZmZpYBwAAAGluaXRfb25xB11x
CFgZAAAAa2VlcF91bmxvY2FsaXplZF9jaGFubmVsc3EJiVgPAAAAbGluZW5vaXNlX2F3YXJlcQqI
WBAAAABtYXhfYmFkX2NoYW5uZWxzcQtHP8MzMzMzMzNYDwAAAG1heF9icm9rZW5fdGltZXEMRz/Z
mZmZmZmaWAgAAABtaW5fY29ycnENRz/gAAAAAAAAWA8AAABub2lzZV90aHJlc2hvbGRxDksEWAsA
AABudW1fc2FtcGxlc3EPS8hYEAAAAHByb3RlY3RfY2hhbm5lbHNxEF1xEShLA0sESxJLE2VYDAAA
AHJlcmVmZXJlbmNlZHESiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXETY3NpcApfdW5waWNrbGVf
dHlwZQpxFFgMAAAAUHlRdDQuUXRDb3JlcRVYCgAAAFFCeXRlQXJyYXlxFkMuAdnQywABAAAAAAR7
AAABGQAABfIAAAOFAAAEgwAAATgAAAXqAAADfQAAAAAAAHEXhXEYh3EZUnEaWA4AAABzZXRfYnJl
YWtwb2ludHEbiVgLAAAAc3Vic2V0X3NpemVxHEc/wzMzMzMzM1gQAAAAdXNlX2NsZWFuX3dpbmRv
d3EdiVgKAAAAd2luZG93X2xlbnEeSwVYFgAAAHdpbmRvd19sZW5fY2xlYW53aW5kb3dxH0c/4AAA
AAAAAFgOAAAAd2luZG93X292ZXJsYXBxIEc/5R64UeuFH1gRAAAAenNjb3JlX3RocmVzaG9sZHNx
IV1xIihHwAwAAAAAAABLBWV1Lg==
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWA4AAABmb3JjZV9vdmVycmlkZXEBiFgHAAAAbW9udGFnZXECWAAAAABxA1gTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlRdDQuUXRDb3Jl
cQZYCgAAAFFCeXRlQXJyYXlxB0MuAdnQywABAAAAAAMCAAABxQAABHkAAAJ1AAADCgAAAeQAAARx
AAACbQAAAAAAAHEIhXEJh3EKUnELWA4AAABzZXRfYnJlYWtwb2ludHEMiXUu
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWBAAAABkZXNpcmVkX2NoYW5uZWxzcQFYDQAAACh1c2UgZGVmYXVsdClxAlgHAAAAbW9u
dGFnZXEDWAAAAABxBFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEFY3NpcApfdW5waWNrbGVfdHlw
ZQpxBlgMAAAAUHlRdDQuUXRDb3JlcQdYCgAAAFFCeXRlQXJyYXlxCEMuAdnQywABAAAAAAREAAAC
QgAABbsAAAL1AAAETAAAAmEAAAWzAAAC7QAAAAAAAHEJhXEKh3ELUnEMWA4AAABzZXRfYnJlYWtw
b2ludHENiXUu
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQFjc2lwCl91bnBpY2tsZV90eXBlCnECWAwA
AABQeVF0NC5RdENvcmVxA1gKAAAAUUJ5dGVBcnJheXEEQy4B2dDLAAEAAAAABEQAAAJ5AAAFuwAA
AvwAAARMAAACmAAABbMAAAL0AAAAAAAAcQWFcQaHcQdScQhYDgAAAHNldF9icmVha3BvaW50cQmJ
dS4=
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQFjc2lwCl91bnBpY2tsZV90eXBlCnECWAwA
AABQeVF0NC5RdENvcmVxA1gKAAAAUUJ5dGVBcnJheXEEQy4B2dDLAAEAAAAABEQAAAJjAAAFuwAA
Av4AAARMAAACggAABbMAAAL2AAAAAAAAcQWFcQaHcQdScQhYDgAAAHNldF9icmVha3BvaW50cQmJ
WAYAAABzdHJlYW1xClgAAAAAcQtYBwAAAHZlcmJvc2VxDIl1Lg==
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAEAAABhcQFYDQAAACh1c2UgZGVmYXVsdClxAlgBAAAAYnEDaAJYCgAAAGJsb2NrX3Np
emVxBEsKWA0AAABjYWxpYl9zZWNvbmRzcQVLLVgGAAAAY3V0b2ZmcQZLFFgPAAAAZW1pdF9jYWxp
Yl9kYXRhcQeIWAcAAABpbml0X29ucQhdcQlYCQAAAGxvb2thaGVhZHEKaAJYEAAAAG1heF9iYWRf
Y2hhbm5lbHNxC0c/yZmZmZmZmlgIAAAAbWF4X2RpbXNxDEsAWBQAAABtYXhfZHJvcG91dF9mcmFj
dGlvbnENRz+5mZmZmZmaWAcAAABtYXhfbWVtcQ5NAAFYEgAAAG1pbl9jbGVhbl9mcmFjdGlvbnEP
Rz/QAAAAAAAAWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cRBjc2lwCl91bnBpY2tsZV90eXBlCnER
WAwAAABQeVF0NC5RdENvcmVxElgKAAAAUUJ5dGVBcnJheXETQy4B2dDLAAEAAAAABUQAAADFAAAG
uwAAA08AAAVMAAAA5AAABrMAAANHAAAAAAAAcRSFcRWHcRZScRdYDgAAAHNldF9icmVha3BvaW50
cRiJWA0AAABzdGRkZXZfY3V0b2ZmcRlLFFgJAAAAc3RlcF9zaXplcRpHP8mZmZmZmZpYEAAAAHVz
ZV9jbGVhbl93aW5kb3dxG4hYCgAAAHVzZV9sZWdhY3lxHIlYFgAAAHdpbmRvd19sZW5fY2xlYW53
aW5kb3dxHUc/4AAAAAAAAFgNAAAAd2luZG93X2xlbmd0aHEeRz/gAAAAAAAAWA4AAAB3aW5kb3df
b3ZlcmxhcHEfRz/lHrhR64UfWBoAAAB3aW5kb3dfb3ZlcmxhcF9jbGVhbndpbmRvd3EgRz/lHrhR
64UfWBEAAAB6c2NvcmVfdGhyZXNob2xkc3EhXXEiKEr7////SwdldS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECS1pYDgAA
AG1heF91cGRhdGVyYXRlcQNN9AFYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlj
a2xlX3R5cGUKcQVYDAAAAFB5UXQ0LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAA
AAAERAAAAnkAAAW7AAADWQAABEwAAAKYAAAFswAAA1EAAAAAAABxCIVxCYdxClJxC1gOAAAAc2V0
X2JyZWFrcG9pbnRxDIlYDgAAAHdhcm11cF9zYW1wbGVzcQ1K/////3Uu
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEc/4AAAAAAAAEsoZVgNAAAAbWluaW11bV9waGFzZXEJiFgEAAAA
bW9kZXEKWAgAAABiYW5kcGFzc3ELWAUAAABvcmRlcnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1YEwAA
AHNhdmVkV2lkZ2V0R2VvbWV0cnlxDmNzaXAKX3VucGlja2xlX3R5cGUKcQ9YDAAAAFB5UXQ0LlF0
Q29yZXEQWAoAAABRQnl0ZUFycmF5cRFDLgHZ0MsAAQAAAAAERAAAAlcAAAW7AAADCgAABEwAAAJ2
AAAFswAAAwIAAAAAAABxEoVxE4dxFFJxFVgOAAAAc2V0X2JyZWFrcG9pbnRxFolYCgAAAHN0b3Bf
YXR0ZW5xF0dASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQFjc2lwCl91bnBpY2tsZV90eXBlCnECWAwA
AABQeVF0NC5RdENvcmVxA1gKAAAAUUJ5dGVBcnJheXEEQy4B2dDLAAEAAAAABEQAAAJ5AAAFuwAA
AucAAARMAAACmAAABbMAAALfAAAAAAAAcQWFcQaHcQdScQhYDgAAAHNldF9icmVha3BvaW50cQmJ
dS4=
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQFjc2lwCl91bnBpY2tsZV90eXBlCnECWAwA
AABQeVF0NC5RdENvcmVxA1gKAAAAUUJ5dGVBcnJheXEEQy4B2dDLAAEAAAAABEQAAAJ5AAAFuwAA
AucAAARMAAACmAAABbMAAALfAAAAAAAAcQWFcQaHcQdScQhYDgAAAHNldF9icmVha3BvaW50cQmJ
dS4=
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiVgOAAAAbWF4X2dhcF9sZW5ndGhxAktkWA8A
AABvbmxpbmVfZXBvY2hpbmdxA1gNAAAAbWFya2VyLWxvY2tlZHEEWA0AAABzYW1wbGVfb2Zmc2V0
cQVLAFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEGY3NpcApfdW5waWNrbGVfdHlwZQpxB1gMAAAA
UHlRdDQuUXRDb3JlcQhYCgAAAFFCeXRlQXJyYXlxCUMuAdnQywABAAAAAAREAAACNAAABbsAAANZ
AAAETAAAAlMAAAWzAAADUQAAAAAAAHEKhXELh3EMUnENWA4AAABzZWxlY3RfbWFya2Vyc3EOWA0A
AAAodXNlIGRlZmF1bHQpcQ9YDgAAAHNldF9icmVha3BvaW50cRCJWAsAAAB0aW1lX2JvdW5kc3ER
XXESKEsASwFlWAcAAAB2ZXJib3NlcROJdS4=
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWBIAAABhbHNvX2xlZ2FjeV9vdXRwdXRxAYlYDgAAAGlzX2NhdGVnb3JpY2FscQKJWAkA
AABpdl9jb2x1bW5xA1gGAAAATWFya2VycQRYBwAAAG1hcHBpbmdxBX1xBihYAgAAAGx2cQdLAFgC
AAAAaHZxCEsBdVgOAAAAbWFwcGluZ19mb3JtYXRxCVgGAAAAY29tcGF0cQpYEwAAAHNhdmVkV2lk
Z2V0R2VvbWV0cnlxC2NzaXAKX3VucGlja2xlX3R5cGUKcQxYDAAAAFB5UXQ0LlF0Q29yZXENWAoA
AABRQnl0ZUFycmF5cQ5DLgHZ0MsAAQAAAAAEZQAAAyUAAAXcAAAEWQAABG0AAANEAAAF1AAABFEA
AAAAAABxD4VxEIdxEVJxElgOAAAAc2V0X2JyZWFrcG9pbnRxE4lYEQAAAHN1cHBvcnRfd2lsZGNh
cmRzcRSJWAsAAAB1c2VfbnVtYmVyc3EViVgHAAAAdmVyYm9zZXEWiXUu
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWAYAAABhbHBoYXNxAV1xAihHP7mZmZmZmZpHP+AAAAAAAABHP/AAAAAAAABLBUdAJAAA
AAAAAGVYDAAAAGJpYXNfc2NhbGluZ3EDRz/wAAAAAAAAWA0AAABjbGFzc193ZWlnaHRzcQRYBAAA
AGF1dG9xBVgKAAAAY29uZF9maWVsZHEGWAsAAABUYXJnZXRWYWx1ZXEHWBAAAABkb250X3Jlc2V0
X21vZGVscQiJWBAAAABkdWFsX2Zvcm11bGF0aW9ucQmJWAwAAABpbmNsdWRlX2JpYXNxCohYDwAA
AGluaXRpYWxpemVfb25jZXELiFgIAAAAbWF4X2l0ZXJxDEtkWAoAAABtdWx0aWNsYXNzcQ1YAwAA
AG92cnEOWAkAAABudW1fZm9sZHNxD0sFWAgAAABudW1fam9ic3EQSwFYDQAAAHByb2JhYmlsaXN0
aWNxEYhYCwAAAHJlZ3VsYXJpemVycRJYAgAAAGwycRNYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlx
FGNzaXAKX3VucGlja2xlX3R5cGUKcRVYDAAAAFB5UXQ0LlF0Q29yZXEWWAoAAABRQnl0ZUFycmF5
cRdDLgHZ0MsAAQAAAAAFEAAAAw8AAAaHAAAD8gAABRgAAAMuAAAGfwAAA+oAAAAAAABxGIVxGYdx
GlJxG1gNAAAAc2VhcmNoX21ldHJpY3EcWAgAAABhY2N1cmFjeXEdWA4AAABzZXRfYnJlYWtwb2lu
dHEeiVgGAAAAc29sdmVycR9YBQAAAGxiZmdzcSBYCQAAAHRvbGVyYW5jZXEhRz8aNuLrHEMtWAkA
AAB2ZXJib3NpdHlxIksAdS4=
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYEQAAAE91dFN0cmVhbS1tYXJrZXJzcQRYEAAAAG1hcmtlcl9zb3VyY2Vf
aWRxBVgAAAAAcQZYDAAAAG1heF9idWZmZXJlZHEHSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFu
Z2VkcQiJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwA
AABQeVF0NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAABEQAAAHxAAAFuwAA
A50AAARMAAACEAAABbMAAAOVAAAAAAAAcQ2FcQ6HcQ9ScRBYDAAAAHNlbmRfbWFya2Vyc3ERiVgO
AAAAc2V0X2JyZWFrcG9pbnRxEolYCQAAAHNvdXJjZV9pZHETaAZYBQAAAHNyYXRlcRRYDQAAACh1
c2UgZGVmYXVsdClxFVgLAAAAc3RyZWFtX25hbWVxFlgQAAAAT3V0U3RyZWFtVmFsZW5jZXEXWAsA
AABzdHJlYW1fdHlwZXEYWAcAAABDb250cm9scRlYEwAAAHVzZV9kYXRhX3RpbWVzdGFtcHNxGohY
FgAAAHVzZV9udW1weV9vcHRpbWl6YXRpb25xG4l1Lg==
</properties>
		<properties format="literal" node_id="15">{'only_nonempty': True, 'print_channel': False, 'print_compact': True, 'print_data': False, 'print_markers': False, 'print_streams': [], 'print_time': False, 'print_trial': False, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWAwAAABiZWdpbl9tYXJrZXJxAVgLAAAAY2FsaWItYmVnaW5xAlgRAAAAY2FsaWJyYXRp
b25fZmlyc3RxA4hYDwAAAGNhbl9yZWNhbGlicmF0ZXEEiVgPAAAAZW1pdF9jYWxpYl9kYXRhcQWI
WBEAAABlbWl0X3ByZWRpY3RfZGF0YXEGiFgKAAAAZW5kX21hcmtlcnEHWAkAAABjYWxpYi1lbmRx
CFgLAAAAbWFya2VyX21vZGVxCVgHAAAAbWFya2Vyc3EKWA0AAABwcmludF9tYXJrZXJzcQuJWBMA
AABzYXZlZFdpZGdldEdlb21ldHJ5cQxjc2lwCl91bnBpY2tsZV90eXBlCnENWAwAAABQeVF0NC5R
dENvcmVxDlgKAAAAUUJ5dGVBcnJheXEPQy4B2dDLAAEAAAAABEQAAAJAAAAFuwAAA4kAAARMAAAC
XwAABbMAAAOBAAAAAAAAcRCFcRGHcRJScRNYDgAAAHNldF9icmVha3BvaW50cRSJWAcAAAB2ZXJi
b3NlcRWJdS4=
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAAERAAAAksAAAW7AAADFgAABEwA
AAJqAAAFswAAAw4AAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxdcQ1LA2FYDgAAAHNl
dF9icmVha3BvaW50cQ6JWAQAAAB1bml0cQ9YBwAAAGluZGljZXNxEHUu
</properties>
		<properties format="literal" node_id="18">{'apply_multiple_axes': False, 'axis': 'time', 'savedWidgetGeometry': None, 'selection': ':', 'set_breakpoint': False, 'unit': 'indices'}</properties>
		<properties format="literal" node_id="19">{'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="20">gAN9cQAoWAkAAABibG9ja3NpemVxAUtkWAsAAABmcmVxdWVuY2llc3ECXXEDKEsESwhlWBMAAABz
YXZlZFdpZGdldEdlb21ldHJ5cQRjc2lwCl91bnBpY2tsZV90eXBlCnEFWAwAAABQeVF0NC5RdENv
cmVxBlgKAAAAUUJ5dGVBcnJheXEHQy4B2dDLAAEAAAAABEQAAAJtAAAFuwAAAvMAAARMAAACjAAA
BbMAAALrAAAAAAAAcQiFcQmHcQpScQtYDgAAAHNldF9icmVha3BvaW50cQyJdS4=
</properties>
		<properties format="pickle" node_id="21">gAN9cQAoWAkAAABibG9ja3NpemVxAUtkWAsAAABmcmVxdWVuY2llc3ECXXEDKEc/4AAAAAAAAEso
ZVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEEY3NpcApfdW5waWNrbGVfdHlwZQpxBVgMAAAAUHlR
dDQuUXRDb3JlcQZYCgAAAFFCeXRlQXJyYXlxB0MuAdnQywABAAAAAAREAAACbQAABbsAAALzAAAE
TAAAAowAAAWzAAAC6wAAAAAAAHEIhXEJh3EKUnELWA4AAABzZXRfYnJlYWtwb2ludHEMiXUu
</properties>
		<properties format="pickle" node_id="22">gAN9cQAoWAkAAABibG9ja3NpemVxAUtkWAsAAABmcmVxdWVuY2llc3ECXXEDKEsESwhlWBMAAABz
YXZlZFdpZGdldEdlb21ldHJ5cQRjc2lwCl91bnBpY2tsZV90eXBlCnEFWAwAAABQeVF0NC5RdENv
cmVxBlgKAAAAUUJ5dGVBcnJheXEHQy4B2dDLAAEAAAAABEQAAAJtAAAFuwAAAvMAAARMAAACjAAA
BbMAAALrAAAAAAAAcQiFcQmHcQpScQtYDgAAAHNldF9icmVha3BvaW50cQyJdS4=
</properties>
		<properties format="literal" node_id="23">{'blocksize': 100, 'frequencies': [8, 12], 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="24">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgGAAAAZGVzaWducQNYBgAAAGJ1dHRlcnEEWAsA
AABmcmVxdWVuY2llc3EFXXEGKEc/uZmZmZmZmkc/4AAAAAAAAEstSzdlWAsAAABpZ25vcmVfbmFu
c3EHiVgEAAAAbW9kZXEIWAgAAABiYW5kc3RvcHEJWBAAAABvZmZsaW5lX2ZpbHRmaWx0cQqJWAUA
AABvcmRlcnELWA0AAAAodXNlIGRlZmF1bHQpcQxYCQAAAHBhc3NfbG9zc3ENR0AIAAAAAAAAWBMA
AABzYXZlZFdpZGdldEdlb21ldHJ5cQ5jc2lwCl91bnBpY2tsZV90eXBlCnEPWAwAAABQeVF0NC5R
dENvcmVxEFgKAAAAUUJ5dGVBcnJheXERQy4B2dDLAAEAAAAAAwQAAAFSAAAEewAAAqcAAAMMAAAB
cQAABHMAAAKfAAAAAAAAcRKFcROHcRRScRVYDgAAAHNldF9icmVha3BvaW50cRaJWAoAAABzdG9w
X2F0dGVucRdHQEkAAAAAAAB1Lg==
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node6",
            "channel_names",
            "node4",
            "desired_channels"
        ],
        [
            "node2",
            "data",
            "node7",
            "data"
        ],
        [
            "node7",
            "data",
            "node4",
            "data"
        ],
        [
            "node1",
            "data",
            "node8",
            "data"
        ],
        [
            "node17",
            "data",
            "node13",
            "data"
        ],
        [
            "node14",
            "data",
            "node16",
            "data"
        ],
        [
            "node14",
            "data",
            "node15",
            "data"
        ],
        [
            "node13",
            "data",
            "node12",
            "data"
        ],
        [
            "node12",
            "data",
            "node18",
            "data"
        ],
        [
            "node12",
            "data",
            "node19",
            "data"
        ],
        [
            "node10",
            "outdata",
            "node11",
            "data1"
        ],
        [
            "node20",
            "outdata",
            "node11",
            "data2"
        ],
        [
            "node3",
            "data",
            "node5",
            "data"
        ],
        [
            "node18",
            "data",
            "node21",
            "data"
        ],
        [
            "node18",
            "data",
            "node22",
            "data"
        ],
        [
            "node21",
            "data",
            "node10",
            "data1"
        ],
        [
            "node22",
            "data",
            "node10",
            "data2"
        ],
        [
            "node19",
            "data",
            "node23",
            "data"
        ],
        [
            "node19",
            "data",
            "node24",
            "data"
        ],
        [
            "node23",
            "data",
            "node20",
            "data1"
        ],
        [
            "node24",
            "data",
            "node20",
            "data2"
        ],
        [
            "node9",
            "data",
            "node17",
            "data"
        ],
        [
            "node25",
            "data",
            "node3",
            "data"
        ],
        [
            "node5",
            "data",
            "node6",
            "data"
        ],
        [
            "node5",
            "data",
            "node2",
            "data"
        ],
        [
            "node4",
            "data",
            "node9",
            "data"
        ],
        [
            "node8",
            "data",
            "node25",
            "data"
        ],
        [
            "node11",
            "outdata",
            "node14",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Fp1",
                        "Fp2",
                        "Fz",
                        "F7",
                        "F8",
                        "FC1",
                        "FC2",
                        "Cz",
                        "C3",
                        "C4",
                        "T7",
                        "T8",
                        "CPz",
                        "CP1",
                        "CP2",
                        "CP5",
                        "CP6",
                        "M1",
                        "M2",
                        "Pz",
                        "P3",
                        "P4",
                        "O1",
                        "O2"
                    ]
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='Unity.MarkersValenceStream'"
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "name='EEG'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "50d432c0-d68e-44bc-8140-70f0dd1cc2a7"
        },
        "node10": {
            "class": "Divide",
            "module": "neuropype.nodes.elementwise_math.Divide",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "37876cce-0aa1-428f-a1df-fa5351fff73c"
        },
        "node11": {
            "class": "Subtract",
            "module": "neuropype.nodes.elementwise_math.Subtract",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "2c0fa673-affe-4cd7-8972-1692479836f4"
        },
        "node12": {
            "class": "Segmentation",
            "module": "neuropype.nodes.formatting.Segmentation",
            "params": {
                "keep_marker_chunk": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "max_gap_length": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 100
                },
                "online_epoching": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "marker-locked"
                },
                "sample_offset": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "select_markers": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_bounds": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        1
                    ]
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "a84794c4-eb38-46b6-b7b3-263ef2ace0ce"
        },
        "node13": {
            "class": "AssignTargets",
            "module": "neuropype.nodes.machine_learning.AssignTargets",
            "params": {
                "also_legacy_output": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "is_categorical": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "mapping": {
                    "customized": true,
                    "type": "Port",
                    "value": {
                        "hv": 1,
                        "lv": 0
                    }
                },
                "mapping_format": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "compat"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "support_wildcards": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "1799947c-66e9-4e80-8fca-415af56092b5"
        },
        "node14": {
            "class": "LogisticRegression",
            "module": "neuropype.nodes.machine_learning.LogisticRegression",
            "params": {
                "alphas": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        0.1,
                        0.5,
                        1.0,
                        5,
                        10.0
                    ]
                },
                "bias_scaling": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "class_weights": {
                    "customized": true,
                    "type": "Port",
                    "value": "auto"
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "dual_formulation": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "include_bias": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_iter": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "multiclass": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "ovr"
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "num_jobs": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "regularizer": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "l2"
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "lbfgs"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "2d686216-9b48-4919-82d7-a4757cbce1c4"
        },
        "node15": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "OutStream-markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "OutStreamValence"
                },
                "stream_type": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Control"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "9b2f1831-a6b2-43fc-94e7-5752593a390c"
        },
        "node16": {
            "class": "PrintToConsole",
            "module": "neuropype.nodes.diagnostics.PrintToConsole",
            "params": {
                "only_nonempty": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "print_channel": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_compact": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "print_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_streams": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "print_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_trial": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "437d0805-5ffd-4215-9877-b0c13322fdb3"
        },
        "node17": {
            "class": "AccumulateCalibrationData",
            "module": "neuropype.nodes.machine_learning.AccumulateCalibrationData",
            "params": {
                "begin_marker": {
                    "customized": false,
                    "type": "Port",
                    "value": "calib-begin"
                },
                "calibration_first": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "can_recalibrate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "emit_calib_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "emit_predict_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "end_marker": {
                    "customized": false,
                    "type": "Port",
                    "value": "calib-end"
                },
                "marker_mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "markers"
                },
                "print_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "82d8de18-5413-4fbb-aad0-f710d3ab496e"
        },
        "node18": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": [
                        3
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "e3a56515-93a8-421d-b544-d8f0117a477c"
        },
        "node19": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "selection": {
                    "customized": false,
                    "type": "Port",
                    "value": ":"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "58dd848c-cbf6-4952-aa13-dd8e6453fa3e"
        },
        "node2": {
            "class": "BadChannelRemoval",
            "module": "neuropype.nodes.neural.BadChannelRemoval",
            "params": {
                "calib_seconds": {
                    "customized": true,
                    "type": "IntPort",
                    "value": 15
                },
                "coords_override": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "corr_threshold": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.8
                },
                "ignore_chanlocs": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "ignored_quantile": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                },
                "init_on": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "keep_unlocalized_channels": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "linenoise_aware": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_bad_channels": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.15
                },
                "max_broken_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.4
                },
                "min_corr": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "noise_threshold": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 4
                },
                "num_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 200
                },
                "protect_channels": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        3,
                        4,
                        18,
                        19
                    ]
                },
                "rereferenced": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "subset_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.15
                },
                "use_clean_window": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "window_len": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "window_len_cleanwindow": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "window_overlap": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.66
                },
                "zscore_thresholds": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        -3.5,
                        5
                    ]
                }
            },
            "uuid": "bd0272f3-e228-44a9-9fe1-c898e6572683"
        },
        "node20": {
            "class": "Divide",
            "module": "neuropype.nodes.elementwise_math.Divide",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "0fcddcfe-2a59-45d5-b2c8-02e338baa06a"
        },
        "node21": {
            "class": "SpectralSelection",
            "module": "neuropype.nodes.spectral.SpectralSelection",
            "params": {
                "blocksize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        4,
                        8
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "587fc307-884d-47d4-a03b-50910a40daa5"
        },
        "node22": {
            "class": "SpectralSelection",
            "module": "neuropype.nodes.spectral.SpectralSelection",
            "params": {
                "blocksize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0.5,
                        40
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "18a2c30a-9aa8-4cc4-bbe8-46560d7583bf"
        },
        "node23": {
            "class": "SpectralSelection",
            "module": "neuropype.nodes.spectral.SpectralSelection",
            "params": {
                "blocksize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        4,
                        8
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "415923fd-7a22-48b6-8e43-4d7ba7e4659e"
        },
        "node24": {
            "class": "SpectralSelection",
            "module": "neuropype.nodes.spectral.SpectralSelection",
            "params": {
                "blocksize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "frequencies": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        8,
                        12
                    ]
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "4bfba898-dee2-464b-977b-60d395a22d46"
        },
        "node25": {
            "class": "IIRFilter",
            "module": "neuropype.nodes.signal_processing.IIRFilter",
            "params": {
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "design": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "butter"
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0.1,
                        0.5,
                        45,
                        55
                    ]
                },
                "ignore_nans": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "mode": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "bandstop"
                },
                "offline_filtfilt": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "pass_loss": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 3.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "5c0ef7fa-29f6-4a63-88ab-e15250fbc5e0"
        },
        "node3": {
            "class": "AssignChannelLocations",
            "module": "neuropype.nodes.source_localization.AssignChannelLocations",
            "params": {
                "force_override": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "montage": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "01bebb1b-cef2-4d9e-b8c8-32fa4e4b5d6f"
        },
        "node4": {
            "class": "InterpolateMissingChannels",
            "module": "neuropype.nodes.neural.InterpolateMissingChannels",
            "params": {
                "desired_channels": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Fp1",
                        "Fp2",
                        "Fz",
                        "F7",
                        "F8",
                        "FC1",
                        "FC2",
                        "Cz",
                        "C3",
                        "C4",
                        "T7",
                        "T8",
                        "CPz",
                        "CP1",
                        "CP2",
                        "CP5",
                        "CP6",
                        "Pz",
                        "P3",
                        "P4",
                        "O1",
                        "O2"
                    ]
                },
                "montage": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "056423f0-575d-4ef1-bedb-a02fa832a0dc"
        },
        "node5": {
            "class": "RemoveUnlocalizedChannels",
            "module": "neuropype.nodes.source_localization.RemoveUnlocalizedChannels",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "8e17eb3c-de80-4261-8443-f253d9a2558a"
        },
        "node6": {
            "class": "ExtractChannels",
            "module": "neuropype.nodes.utilities.ExtractChannels",
            "params": {
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "1054dfee-ed1e-4d2f-8e7d-aa0bbd6b6617"
        },
        "node7": {
            "class": "ArtifactRemoval",
            "module": "neuropype.nodes.neural.ArtifactRemoval",
            "params": {
                "a": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "b": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "block_size": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 10
                },
                "calib_seconds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 45
                },
                "cutoff": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 20
                },
                "emit_calib_data": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "init_on": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "lookahead": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "max_bad_channels": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "max_dims": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0
                },
                "max_dropout_fraction": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.1
                },
                "max_mem": {
                    "customized": false,
                    "type": "Port",
                    "value": 256
                },
                "min_clean_fraction": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.25
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stddev_cutoff": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 20
                },
                "step_size": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "use_clean_window": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_legacy": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "window_len_cleanwindow": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "window_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "window_overlap": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.66
                },
                "window_overlap_cleanwindow": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.66
                },
                "zscore_thresholds": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        -5,
                        7
                    ]
                }
            },
            "uuid": "fefdee9c-cde4-4d68-b164-3a530915062e"
        },
        "node8": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 90
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "e43a03f8-136c-4da8-9364-23e295de2bbc"
        },
        "node9": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0.5,
                        40
                    ]
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "366ee6b1-a306-456c-be81-879f8b98d7e2"
        }
    },
    "version": 1.1
}</patch>
</scheme>
