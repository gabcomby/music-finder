import websiteText from "@/assets/websiteText";
import { Button } from "../ui/button";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "../ui/dialog";
import { Label } from "../ui/label";
import { Input } from "../ui/input";
import {
  Dropzone,
  DropzoneContent,
  DropzoneEmptyState,
} from "../ui/shadcn-io/dropzone";
import { useState } from "react";
import { Music4 } from "lucide-react";

const SongAdder = () => {
  // For file uploader
  const [files, setFiles] = useState<File[] | undefined>();
  const handleDrop = (files: File[]) => {
    console.log(files);
    setFiles(files);
  };

  return (
    <div className="flex flex-col w-1/6 gap-4">
      <p className="text-muted-foreground text-sm text-center">
        {websiteText.newSongAdderText}
      </p>
      <Dialog>
        <form>
          <DialogTrigger asChild className="w-full">
            <Button variant="default">
              <Music4 />
              {websiteText.addSongButton}
            </Button>
          </DialogTrigger>
          <DialogContent className="sm:max-w-[425px]">
            <DialogHeader>
              <DialogTitle>{websiteText.uploadNewSongTitle}</DialogTitle>
              <DialogDescription>
                {websiteText.uploadNewSongDescription}
              </DialogDescription>
            </DialogHeader>
            <div className="grid gap-4">
              <div className="grid gap-3">
                <Label htmlFor="songName-1">{websiteText.songTitleLabel}</Label>
                <Input
                  id="songName-1"
                  name="songName"
                  placeholder={websiteText.rollingInTheDeep}
                />
              </div>
              <div className="grid gap-3">
                <Label htmlFor="artistName-1">{websiteText.artistLabel}</Label>
                <Input
                  id="artistName-1"
                  name="artistName"
                  placeholder={websiteText.adele}
                />
              </div>
              <div className="grid gap-3">
                <Label>{websiteText.audioFileLabel}</Label>
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
            </div>
            <DialogFooter>
              <DialogClose asChild>
                <Button variant="outline">{websiteText.cancel}</Button>
              </DialogClose>
              <Button type="submit">{websiteText.saveChanges}</Button>
            </DialogFooter>
          </DialogContent>
        </form>
      </Dialog>
    </div>
  );
};

export default SongAdder;
