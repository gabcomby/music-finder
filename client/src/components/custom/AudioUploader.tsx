import { Button } from "../ui/button";
import { Mic } from "lucide-react";
import { Square } from "lucide-react";
import {
  Dropzone,
  DropzoneContent,
  DropzoneEmptyState,
} from "@/components/ui/shadcn-io/dropzone";
// import { useState } from "react";
import { useAudioRecorder } from "@fixhq/react-audio-voice-recorder";
import websiteText from "@/assets/websiteText";
import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/",
});

const AudioUploader = () => {
  // For file uploader
  // const [files, setFiles] = useState<File[] | undefined>();
  const handleDrop = async (files: File[]) => {
    //console.log(files);
    //setFiles(files);
    const formData = new FormData();
    formData.append("file", files[0]);
    const res = await api.post("search", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });
    console.log(res.data);
  };

  // For live audio recorder
  const {
    startRecording,
    stopRecording,
    recordingBlob,
    isRecording,
    recordingTime,
  } = useAudioRecorder();

  return (
    <div className="flex flex-col w-1/6 gap-4">
      {isRecording ? (
        <Button
          variant="outline"
          size="sm"
          onClick={() => {
            stopRecording();
            if (recordingBlob) console.log(recordingBlob);
          }}
        >
          <Square /> {websiteText.stopRecordingButton} ({recordingTime}s)
        </Button>
      ) : (
        <Button variant="outline" size="sm" onClick={startRecording}>
          <Mic /> {websiteText.recordLiveAudioButton}
        </Button>
      )}
      <h4 className="scroll-m-20 text-xl font-semibold tracking-tight text-center">
        {websiteText.orText}
      </h4>
      <Dropzone
        maxFiles={1}
        maxSize={1024 * 1024 * 10}
        minSize={1024}
        onDrop={handleDrop}
        onError={console.error}
        // src={files}
      >
        <DropzoneEmptyState />
        <DropzoneContent />
      </Dropzone>
    </div>
  );
};

export default AudioUploader;
