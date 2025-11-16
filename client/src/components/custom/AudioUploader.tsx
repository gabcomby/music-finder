import { Button } from "../ui/button";
import { Mic } from "lucide-react";
import { Square } from "lucide-react";
import {
  Dropzone,
  DropzoneContent,
  DropzoneEmptyState,
} from "@/components/ui/shadcn-io/dropzone";
import { useState } from "react";
import { useAudioRecorder } from "@fixhq/react-audio-voice-recorder";

const AudioUploader = () => {
  // For file uploader
  const [files, setFiles] = useState<File[] | undefined>();
  const handleDrop = (files: File[]) => {
    console.log(files);
    setFiles(files);
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
          <Square /> Stop Recording ({recordingTime}s)
        </Button>
      ) : (
        <Button variant="outline" size="sm" onClick={startRecording}>
          <Mic /> Record Live Audio
        </Button>
      )}
      <h4 className="scroll-m-20 text-xl font-semibold tracking-tight text-center">
        or
      </h4>
      <Dropzone
        maxFiles={1}
        maxSize={1024 * 1024 * 10}
        minSize={1024}
        onDrop={handleDrop}
        onError={console.error}
        src={files}
      >
        <DropzoneEmptyState />
        <DropzoneContent />
      </Dropzone>
    </div>
  );
};

export default AudioUploader;
