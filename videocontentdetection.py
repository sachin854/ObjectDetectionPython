from google.cloud import videointelligence

def detect_objects(video_uri):
    client = videointelligence.VideoIntelligenceServiceClient()

    # Configure the video context for object tracking
    config = videointelligence.ObjectTrackingConfig()

    # Perform asynchronous video annotation
    operation = client.annotate_video(
        input_uri=video_uri,
        features=[videointelligence.Feature.OBJECT_TRACKING],
        video_context=config,
    )

    print("Processing video for object detection annotations...")

    # Wait for the operation to complete
    result = operation.result(timeout=600)  # Set the timeout according to your video's length

    print("\nFinished processing.\n")

    # Process the results
    for annotation_result in result.annotation_results:
        for track in annotation_result.object_annotations:
            print(f"Object: {track.entity.description}")
            print("Segment:")
            for timestamped_object in track.frames:
                start_time = (
                    timestamped_object.time_offset.seconds
                    + timestamped_object.time_offset.nanos / 1e9
                )
                end_time = (
                    timestamped_object.time_offset.seconds
                    + timestamped_object.time_offset.nanos / 1e9
                    + timestamped_object.time_offset_end.seconds
                    + timestamped_object.time_offset_end.nanos / 1e9
                )
                print(f"\t{start_time:.2f}s to {end_time:.2f}s")
            print()

# Replace 'your_video_uri' with the GCS URI of your video
video_uri = "gs://your-bucket-name/your-video.mp4"
detect_objects(video_uri)
