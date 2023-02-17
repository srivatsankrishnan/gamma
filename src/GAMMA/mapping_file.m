Network 0 {
Layer CONV {
Type: CONV
Dimensions { K: 64, C: 3, Y: 224, X: 224, R: 7, S: 7 }
Dataflow {
TemporalMap(7,7) R;
TemporalMap(60,60) K;
SpatialMap(198,198) X';
TemporalMap(2,2) C;
TemporalMap(7,7) Y';
TemporalMap(7,7) S;
Cluster(2,P);
TemporalMap(1,1) X';
TemporalMap(1,1) Y';
TemporalMap(7,7) R;
SpatialMap(1,1) C;
TemporalMap(1,1) K;
TemporalMap(7,7) S;
}
}
}