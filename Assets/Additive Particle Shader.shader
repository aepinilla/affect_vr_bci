// Shader created with Shader Forge v1.40 
// Shader Forge (c) Freya Holmer - http://www.acegikmo.com/shaderforge/
// Note: Manually altering this data may prevent you from opening it in Shader Forge
/*SF_DATA;ver:1.40;sub:START;pass:START;ps:flbk:,iptp:0,cusa:False,bamd:0,cgin:,cpap:True,lico:1,lgpr:1,limd:0,spmd:1,trmd:0,grmd:0,uamb:True,mssp:True,bkdf:False,hqlp:False,rprd:False,enco:False,rmgx:True,imps:True,rpth:0,vtps:0,hqsc:True,nrmq:1,nrsp:0,vomd:0,spxs:False,tesm:0,olmd:1,culm:0,bsrc:0,bdst:0,dpts:2,wrdp:False,dith:0,atcv:False,rfrpo:True,rfrpn:Refraction,coma:15,ufog:True,aust:True,igpj:True,qofs:0,qpre:3,rntp:2,fgom:False,fgoc:True,fgod:False,fgor:False,fgmd:0,fgcr:0.5,fgcg:0.5,fgcb:0.5,fgca:1,fgde:0.01,fgrn:0,fgrf:300,stcl:False,atwp:False,stva:128,stmr:255,stmw:255,stcp:6,stps:0,stfa:0,stfz:0,ofsf:0,ofsu:0,f2p0:False,fnsp:True,fnfb:True,fsmp:False;n:type:ShaderForge.SFN_Final,id:4795,x:32724,y:32693,varname:node_4795,prsc:2|emission-2393-OUT;n:type:ShaderForge.SFN_Tex2d,id:6074,x:32235,y:32601,ptovrint:False,ptlb:MainTex,ptin:_MainTex,varname:_MainTex,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:b7a9e45084e6f4bc88405ab463d350f9,ntxv:0,isnm:False|UVIN-9762-OUT;n:type:ShaderForge.SFN_Multiply,id:2393,x:32495,y:32793,varname:node_2393,prsc:2|A-6074-RGB,B-2053-RGB,C-797-RGB,D-9248-OUT,E-1624-OUT;n:type:ShaderForge.SFN_VertexColor,id:2053,x:32176,y:32762,varname:node_2053,prsc:2;n:type:ShaderForge.SFN_Color,id:797,x:32235,y:32930,ptovrint:True,ptlb:Color,ptin:_TintColor,varname:_TintColor,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,c1:1,c2:1,c3:1,c4:1;n:type:ShaderForge.SFN_Vector1,id:9248,x:32235,y:33081,varname:node_9248,prsc:2,v1:2;n:type:ShaderForge.SFN_Time,id:5958,x:31408,y:32736,varname:node_5958,prsc:2;n:type:ShaderForge.SFN_ValueProperty,id:327,x:31420,y:32572,ptovrint:False,ptlb:U Speed (Main),ptin:_USpeedMain,varname:node_327,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:0.1;n:type:ShaderForge.SFN_ValueProperty,id:3162,x:31443,y:32432,ptovrint:False,ptlb:V Speed (Main),ptin:_VSpeedMain,varname:node_3162,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:0.1;n:type:ShaderForge.SFN_Append,id:9111,x:31668,y:32472,varname:node_9111,prsc:2|A-3162-OUT,B-327-OUT;n:type:ShaderForge.SFN_Multiply,id:4608,x:31813,y:32605,varname:node_4608,prsc:2|A-9111-OUT,B-5958-T;n:type:ShaderForge.SFN_Add,id:9762,x:32029,y:32589,varname:node_9762,prsc:2|A-1716-OUT,B-4608-OUT;n:type:ShaderForge.SFN_Multiply,id:1624,x:32442,y:33168,varname:node_1624,prsc:2|A-6074-A,B-539-R;n:type:ShaderForge.SFN_Tex2d,id:539,x:32057,y:33230,ptovrint:False,ptlb:node_539,ptin:_node_539,varname:node_539,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:5d749cd63bac64fce8e0bc975e19f397,ntxv:0,isnm:False;n:type:ShaderForge.SFN_Time,id:6377,x:30335,y:32419,varname:node_6377,prsc:2;n:type:ShaderForge.SFN_ValueProperty,id:1103,x:30275,y:32742,ptovrint:False,ptlb:U Speed (Noise),ptin:_USpeedNoise,varname:node_1103,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:0.1;n:type:ShaderForge.SFN_ValueProperty,id:5756,x:30442,y:32835,ptovrint:False,ptlb:V Speed (Noise),ptin:_VSpeedNoise,varname:node_5756,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,v1:0.1;n:type:ShaderForge.SFN_Multiply,id:3561,x:30633,y:32439,varname:node_3561,prsc:2|A-6377-T,B-9616-OUT;n:type:ShaderForge.SFN_Append,id:9616,x:30577,y:32628,varname:node_9616,prsc:2|A-1103-OUT,B-5756-OUT;n:type:ShaderForge.SFN_TexCoord,id:5762,x:30726,y:32219,varname:node_5762,prsc:2,uv:0,uaff:False;n:type:ShaderForge.SFN_Add,id:805,x:30911,y:32440,varname:node_805,prsc:2|A-5762-UVOUT,B-3561-OUT;n:type:ShaderForge.SFN_Tex2d,id:5274,x:31117,y:32363,ptovrint:False,ptlb:Noise Tex,ptin:_NoiseTex,varname:node_5274,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:b44dd29ef686d4473be10b1340c79ef5,ntxv:0,isnm:False|UVIN-805-OUT;n:type:ShaderForge.SFN_Slider,id:5935,x:30947,y:32639,ptovrint:False,ptlb:Noise Amount,ptin:_NoiseAmount,varname:node_5935,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,min:0,cur:0.05974546,max:1;n:type:ShaderForge.SFN_Lerp,id:845,x:31574,y:32134,varname:node_845,prsc:2|A-1262-UVOUT,B-5274-R,T-5935-OUT;n:type:ShaderForge.SFN_TexCoord,id:1262,x:31117,y:32078,varname:node_1262,prsc:2,uv:0,uaff:False;n:type:ShaderForge.SFN_Lerp,id:1716,x:32020,y:32087,varname:node_1716,prsc:2|A-7971-UVOUT,B-845-OUT,T-6057-R;n:type:ShaderForge.SFN_Tex2d,id:6057,x:31683,y:32298,ptovrint:False,ptlb:Noise Mask,ptin:_NoiseMask,varname:node_6057,prsc:2,glob:False,taghide:False,taghdr:False,tagprd:False,tagnsco:False,tagnrm:False,tex:5487e500ff3f242be8f2245a194f541c,ntxv:0,isnm:False;n:type:ShaderForge.SFN_TexCoord,id:7971,x:31650,y:31883,varname:node_7971,prsc:2,uv:0,uaff:False;proporder:6074-797-327-3162-539-5274-5935-1103-5756-6057;pass:END;sub:END;*/

Shader "Shader Forge/Additive Particle Shader" {
    Properties {
        _MainTex ("MainTex", 2D) = "white" {}
        _TintColor ("Color", Color) = (1,1,1,1)
        _USpeedMain ("U Speed (Main)", Float ) = 0.1
        _VSpeedMain ("V Speed (Main)", Float ) = 0.1
        _node_539 ("node_539", 2D) = "white" {}
        _NoiseTex ("Noise Tex", 2D) = "white" {}
        _NoiseAmount ("Noise Amount", Range(0, 1)) = 0.05974546
        _USpeedNoise ("U Speed (Noise)", Float ) = 0.1
        _VSpeedNoise ("V Speed (Noise)", Float ) = 0.1
        _NoiseMask ("Noise Mask", 2D) = "white" {}
    }
    SubShader {
        Tags {
            "IgnoreProjector"="True"
            "Queue"="Transparent"
            "RenderType"="Transparent"
        }
        Pass {
            Name "FORWARD"
            Tags {
                "LightMode"="ForwardBase"
            }
            Blend One One
            ZWrite Off
            
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #pragma multi_compile_instancing
            #include "UnityCG.cginc"
            #pragma multi_compile_fwdbase
            #pragma multi_compile_fog
            #pragma target 3.0
            uniform sampler2D _MainTex; uniform float4 _MainTex_ST;
            uniform sampler2D _node_539; uniform float4 _node_539_ST;
            uniform sampler2D _NoiseTex; uniform float4 _NoiseTex_ST;
            uniform sampler2D _NoiseMask; uniform float4 _NoiseMask_ST;
            UNITY_INSTANCING_BUFFER_START( Props )
                UNITY_DEFINE_INSTANCED_PROP( float4, _TintColor)
                UNITY_DEFINE_INSTANCED_PROP( float, _USpeedMain)
                UNITY_DEFINE_INSTANCED_PROP( float, _VSpeedMain)
                UNITY_DEFINE_INSTANCED_PROP( float, _USpeedNoise)
                UNITY_DEFINE_INSTANCED_PROP( float, _VSpeedNoise)
                UNITY_DEFINE_INSTANCED_PROP( float, _NoiseAmount)
            UNITY_INSTANCING_BUFFER_END( Props )
            struct VertexInput {
                UNITY_VERTEX_INPUT_INSTANCE_ID
                float4 vertex : POSITION;
                float2 texcoord0 : TEXCOORD0;
                float4 vertexColor : COLOR;
            };
            struct VertexOutput {
                float4 pos : SV_POSITION;
                UNITY_VERTEX_INPUT_INSTANCE_ID
                float2 uv0 : TEXCOORD0;
                float4 vertexColor : COLOR;
                UNITY_FOG_COORDS(1)
            };
            VertexOutput vert (VertexInput v) {
                VertexOutput o = (VertexOutput)0;
                UNITY_SETUP_INSTANCE_ID( v );
                UNITY_TRANSFER_INSTANCE_ID( v, o );
                o.uv0 = v.texcoord0;
                o.vertexColor = v.vertexColor;
                o.pos = UnityObjectToClipPos( v.vertex );
                UNITY_TRANSFER_FOG(o,o.pos);
                return o;
            }
            float4 frag(VertexOutput i) : COLOR {
                UNITY_SETUP_INSTANCE_ID( i );
////// Lighting:
////// Emissive:
                float4 node_6377 = _Time;
                float _USpeedNoise_var = UNITY_ACCESS_INSTANCED_PROP( Props, _USpeedNoise );
                float _VSpeedNoise_var = UNITY_ACCESS_INSTANCED_PROP( Props, _VSpeedNoise );
                float2 node_805 = (i.uv0+(node_6377.g*float2(_USpeedNoise_var,_VSpeedNoise_var)));
                float4 _NoiseTex_var = tex2D(_NoiseTex,TRANSFORM_TEX(node_805, _NoiseTex));
                float _NoiseAmount_var = UNITY_ACCESS_INSTANCED_PROP( Props, _NoiseAmount );
                float4 _NoiseMask_var = tex2D(_NoiseMask,TRANSFORM_TEX(i.uv0, _NoiseMask));
                float _VSpeedMain_var = UNITY_ACCESS_INSTANCED_PROP( Props, _VSpeedMain );
                float _USpeedMain_var = UNITY_ACCESS_INSTANCED_PROP( Props, _USpeedMain );
                float4 node_5958 = _Time;
                float2 node_9762 = (lerp(i.uv0,lerp(i.uv0,float2(_NoiseTex_var.r,_NoiseTex_var.r),_NoiseAmount_var),_NoiseMask_var.r)+(float2(_VSpeedMain_var,_USpeedMain_var)*node_5958.g));
                float4 _MainTex_var = tex2D(_MainTex,TRANSFORM_TEX(node_9762, _MainTex));
                float4 _TintColor_var = UNITY_ACCESS_INSTANCED_PROP( Props, _TintColor );
                float4 _node_539_var = tex2D(_node_539,TRANSFORM_TEX(i.uv0, _node_539));
                float3 emissive = (_MainTex_var.rgb*i.vertexColor.rgb*_TintColor_var.rgb*2.0*(_MainTex_var.a*_node_539_var.r));
                float3 finalColor = emissive;
                fixed4 finalRGBA = fixed4(finalColor,1);
                UNITY_APPLY_FOG_COLOR(i.fogCoord, finalRGBA, fixed4(0.5,0.5,0.5,1));
                return finalRGBA;
            }
            ENDCG
        }
    }
    CustomEditor "ShaderForgeMaterialInspector"
}
