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
import { useQueryClient, useMutation } from "@tanstack/react-query";
import { useState } from "react";
import type { SearchResult } from "@/schemas/schemas";
import { Skeleton } from "../ui/skeleton";
import ShowResults from "./ShowResults";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/",
});

const AudioUploader = () => {
  const queryClient = useQueryClient();
  // For file uploader
  const [results, setResults] = useState<SearchResult | undefined>();

  const { mutate, isPending, isSuccess, isIdle } = useMutation({
    mutationFn: async (files: File[]) => {
      try {
        const formData = new FormData();
        formData.append("file", files[0]);
        const res = await api.post("search", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
        setResults(res.data);
      } catch (error) {
        if (axios.isAxiosError(error) && error.response) {
          throw error;
        }
        throw error;
      }
    },
  });

  const handleDrop = async (files: File[]) => {
    mutate(files);
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
    <div className="flex flex-col gap-4">
      {isPending && <Skeleton className="w-[200px] h-[200px]" />}
      {isSuccess && results != undefined && <ShowResults results={results} />}
      {isIdle && (
        <>
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
        </>
      )}
    </div>
  );
};

export default AudioUploader;
