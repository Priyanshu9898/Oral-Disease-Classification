import React, { FC } from 'react'
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

const ImageInput:FC = () => {
  return (
    <div className="grid w-full max-w-sm items-center gap-1.5">
      <Label htmlFor="picture">Upload Image</Label>
      <Input id="picture" type="file" />
    </div>
  )
}

export default ImageInput